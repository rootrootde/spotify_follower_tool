import configparser
import sys
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QMainWindow,
    QTableWidgetItem,
    QVBoxLayout,
)
from qtwidgets import AnimatedToggle

import spotipy
from main_window import Ui_MainWindow
from spotipy.oauth2 import SpotifyOAuth

# HOST, PORT = "127.0.0.1", 8888


class SelectPlaylistsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Playlists")
        self.checkboxes = []

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()

        for playlist in self.parent().playlists:
            c = QCheckBox(playlist["name"])
            self.checkboxes.append(c)
            self.layout.addWidget(c)

        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    user_authenticated = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.load_config()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tbl_artists.hideColumn(2)
        self.ui.status_bar.setVisible(True)
        self.ui.le_client_id.setText(self.client_id)
        self.ui.le_client_secret.setText(self.client_secret)

        self.playlists = []
        self.selected_playlists = []
        self.all_playlist_artists = {}

        self.connect_signals()

    def connect_signals(self):
        self.user_authenticated.connect(self.on_user_authenticated)
        self.ui.btn_auth.clicked.connect(self.on_auth)
        self.ui.btn_select_playlists.clicked.connect(self.on_select_playlists)
        self.ui.btn_follow_all.clicked.connect(self.on_follow_all)
        self.ui.btn_unfollow_all.clicked.connect(self.on_unfollow_all)

    def load_config(self):
        self.config = configparser.ConfigParser()
        configfile = Path(__file__).resolve().with_name("config.ini")
        self.config.read(configfile)

        self.client_id = self.config["DEFAULT"]["SPOTIFY_CLIENT_ID"]
        self.client_secret = self.config["DEFAULT"]["SPOTIFY_CLIENT_SECRET"]
        self.redirect_uri = self.config["DEFAULT"]["SPOTIFY_REDIRECT_URI"]

    def save_config(self):
        self.config["DEFAULT"]["SPOTIFY_CLIENT_ID"] = self.client_id
        self.config["DEFAULT"]["SPOTIFY_CLIENT_SECRET"] = self.client_secret
        self.config["DEFAULT"]["SPOTIFY_REDIRECT_URI"] = self.redirect_uri

        with open("config.ini", "w") as configfile:
            self.config.write(configfile)

    def on_item_clicked(self, follow_status, artist_id, artist_name):
        if not follow_status:
            self.follow_artist(artist_id)
        else:
            self.unfollow_artist(artist_id)

    def on_auth(self):
        scope = "user-library-read,user-follow-modify,user-follow-read,playlist-read-private,playlist-read-collaborative"
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.redirect_uri,
                scope=scope,
            )
        )

        current_user = self.sp.current_user()
        self.user_authenticated.emit(current_user["display_name"])

    def on_follow_all(self):
        unchecked_rows = self.get_unchecked_rows()
        artist_ids = [x[2] for x in unchecked_rows]
        self.follow_artist(artist_ids)
        for idx, artist_name, artist_id in unchecked_rows:
            self.ui.tbl_artists.cellWidget(idx, 0).setChecked(True)

    def on_unfollow_all(self):
        checked_rows = self.get_checked_rows()
        artist_ids = [x[2] for x in checked_rows]
        self.unfollow_artist(artist_ids)
        for idx, artist_name, artist_id in checked_rows:
            self.ui.tbl_artists.cellWidget(idx, 0).setChecked(False)

    def on_user_authenticated(self, display_name):
        self.ui.status_bar.setVisible(True)
        self.ui.status_bar.showMessage(f"authenticated as: {display_name}")

    def on_select_playlists(self):
        current_user_playlists = self.sp.current_user_playlists()
        playlists = current_user_playlists["items"]

        dlg = SelectPlaylistsDialog(parent=self)

        if dlg.exec():
            self.selected_playlists = []
            for checkbox in dlg.checkboxes:
                if checkbox.isChecked():
                    for playlist in playlists:
                        if playlist["name"] == checkbox.text():
                            print(f"checked: {playlist['name']} -- {checkbox.text()}")
                            self.selected_playlists.append(playlist)

        if self.selected_playlists:
            self.process_selected_playlists()

    def process_selected_playlists(self):
        for playlist in self.selected_playlists:
            print(f"processing playlist {playlist}")
            playlist_artists = self.get_playlist_artists(playlist)

            for artist in playlist_artists:
                if artist["id"] not in self.all_playlist_artists.keys():
                    self.all_playlist_artists[artist["id"]] = artist

        artists_rows = self.check_follow_status(self.all_playlist_artists.values())

        self.populate_table(artists_rows)

        self.ui.status_bar.showMessage(
            f"found {len(artists_rows)} Artists in {len(self.selected_playlists)} Playlists!"
        )

    def get_playlist_artists(self, playlist):
        playlist_tracks = self.sp.playlist_tracks(playlist["id"])
        playlist_artists = []
        for item in playlist_tracks["items"]:
            for artist in item["track"]["artists"]:
                if artist["id"] not in playlist_artists:
                    playlist_artists.append(artist)

        return playlist_artists

    def check_follow_status(self, artists):
        artists_ids = [artist["id"] for artist in artists]
        artists_names = [artist["name"] for artist in artists]
        chunks = [artists_ids[x : x + 49] for x in range(0, len(artists_ids), 49)]
        result = []
        for chunk in chunks:
            follow_status = self.sp.current_user_following_artists(chunk)
            result.extend(follow_status)

        return list(zip(result, artists_names, artists_ids))

    def follow_artist(self, artist_ids):
        print(f"following: {artist_ids}")
        if isinstance(artist_ids, str):
            self.sp.user_follow_artists([artist_ids])
        else:
            self.sp.user_follow_artists(artist_ids)

    def unfollow_artist(self, artist_ids):
        print(f"unfollowing: {artist_ids}")
        if isinstance(artist_ids, str):
            self.sp.user_unfollow_artists([artist_ids])
        else:
            self.sp.user_unfollow_artists(artist_ids)

    def populate_table(self, rows):
        self.ui.tbl_artists.clearContents()
        self.ui.tbl_artists.setRowCount(len(rows))

        for idx, (follow_status, artist_name, artist_id) in enumerate(rows):
            # toggle = AnimatedToggle(checked_color="#1db954", pulse_checked_color="#44FFB000")
            toggle = AnimatedToggle()

            if follow_status:
                toggle.setCheckState(Qt.CheckState.Checked)
            else:
                toggle.setCheckState(Qt.CheckState.Unchecked)

            self.ui.tbl_artists.setItem(idx, 1, QTableWidgetItem(artist_name))
            self.ui.tbl_artists.setItem(idx, 2, QTableWidgetItem(artist_id))
            self.ui.tbl_artists.setCellWidget(idx, 0, toggle)
            self.ui.tbl_artists.setRowHeight(idx, 40)

            toggle.clicked.connect(
                lambda *args, follow_status=follow_status, artist_id=artist_id, artist_name=artist_name: self.on_item_clicked(
                    follow_status, artist_id, artist_name
                )
            )

        self.ui.tbl_artists.resizeColumnsToContents()

    def get_checked_rows(self):
        checked_rows = []
        for idx in range(self.ui.tbl_artists.rowCount()):
            if self.ui.tbl_artists.cellWidget(idx, 0).isChecked():
                artist_name = self.ui.tbl_artists.item(idx, 1).text()
                artist_id = self.ui.tbl_artists.item(idx, 2).text()
                checked_rows.append((idx, artist_name, artist_id))
        return checked_rows

    def get_unchecked_rows(self):
        unchecked_rows = []
        for idx in range(self.ui.tbl_artists.rowCount()):
            if not self.ui.tbl_artists.cellWidget(idx, 0).isChecked():
                artist_name = self.ui.tbl_artists.item(idx, 1).text()
                artist_id = self.ui.tbl_artists.item(idx, 2).text()
                unchecked_rows.append((idx, artist_name, artist_id))
        return unchecked_rows


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())
