import sys
import os

# Essential stability flags
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu --no-sandbox --disable-software-rasterizer"

from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QPushButton, QLineEdit, QLabel)
from PyQt6.QtWebEngineWidgets import QWebEngineView

class RobloxRetroBlackIcons(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Free Games at ROBLOX.com - Browser")
        self.resize(1280, 800)

        # Updated Stylesheet with Black Symbols
        self.setStyleSheet("""
            QMainWindow { 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #7fb2e5, stop:1 #ffffff); 
            }
            QWidget#TopBar {
                background: #eef3fa;
                border-bottom: 1px solid #99bbe8;
            }
            QWidget#Dashboard {
                background: rgba(255, 255, 255, 0.8);
                border-right: 1px solid #99bbe8;
            }
            QPushButton#DashLink {
                background: transparent; border: none; color: #003366;
                text-align: left; font-family: 'Verdana'; font-size: 11px;
                text-decoration: underline; margin: 2px;
            }
            QPushButton#DashLink:hover { color: #ff6600; }
            
            /* The Nav Buttons with BLACK symbols */
            QPushButton#NavBtn { 
                border: 1px solid #707070; 
                background: #f0f0f0; 
                padding: 1px 5px; 
                font-family: 'Arial'; 
                font-size: 14px;
                font-weight: bold;
                color: black; /* This makes the symbols black */
            }
            
            QLineEdit#Addr { 
                border: 1px solid #7f9db9; background: white; 
                color: black; font-family: 'Verdana'; font-size: 11px;
            }
            QPushButton#GoBtn {
                background: #4CAF50; color: white; border: 1px solid #2e7d32;
                font-weight: bold; font-size: 10px; padding: 1px 8px;
            }
        """)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- TOOLBAR ---
        top_bar = QWidget(); top_bar.setObjectName("TopBar"); top_bar.setFixedHeight(60)
        top_layout = QVBoxLayout(top_bar)

        nav_row = QHBoxLayout()
        # Buttons with Black Symbols
        self.b_back = QPushButton("←"); self.b_back.setObjectName("NavBtn")
        self.b_next = QPushButton("→"); self.b_next.setObjectName("NavBtn")
        self.b_ref = QPushButton("↻"); self.b_ref.setObjectName("NavBtn")
        self.b_home = QPushButton("🏠"); self.b_home.setObjectName("NavBtn")
        
        nav_row.addWidget(self.b_back); nav_row.addWidget(self.b_next)
        nav_row.addWidget(self.b_ref); nav_row.addWidget(self.b_home)
        
        nav_row.addWidget(QLabel(" Address "))
        self.url_bar = QLineEdit(); self.url_bar.setObjectName("Addr")
        nav_row.addWidget(self.url_bar)
        
        self.btn_go = QPushButton("Go"); self.btn_go.setObjectName("GoBtn")
        nav_row.addWidget(self.btn_go)
        top_layout.addLayout(nav_row)

        main_layout.addWidget(top_bar)

        # --- CONTENT AREA ---
        content_area = QHBoxLayout()
        
        # Retro Sidebar Dashboard
        self.sidebar = QWidget(); self.sidebar.setObjectName("Dashboard")
        self.sidebar.setFixedWidth(160)
        side_layout = QVBoxLayout(self.sidebar)
        side_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        side_layout.addWidget(QLabel("<b>MY ROBLOX</b>"))
        
        links = {
            "Home": "https://www.roblox.com/home",
            "Games": "https://www.roblox.com/discover",
            "Catalog": "https://www.roblox.com/catalog",
            "Avatar": "https://www.roblox.com/my/avatar",
            "YouTube": "https://www.youtube.com"
        }

        for name, url in links.items():
            btn = QPushButton(name); btn.setObjectName("DashLink")
            btn.clicked.connect(lambda ch, u=url: self.browser.setUrl(QUrl(u)))
            side_layout.addWidget(btn)

        # Browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://Google.com"))
        
        content_area.addWidget(self.sidebar)
        content_area.addWidget(self.browser)
        main_layout.addLayout(content_area)

        # Logic
        self.b_back.clicked.connect(self.browser.back)
        self.b_next.clicked.connect(self.browser.forward)
        self.b_ref.clicked.connect(self.browser.reload)
        self.b_home.clicked.connect(lambda: self.browser.setUrl(QUrl("https://www.Google.com")))
        self.btn_go.clicked.connect(self.nav)
        self.url_bar.returnPressed.connect(self.nav)
        self.browser.urlChanged.connect(lambda q: self.url_bar.setText(q.toString()))

    def nav(self):
        u = self.url_bar.text()
        if not u.startswith("http"): u = "https://" + u
        self.browser.setUrl(QUrl(u))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobloxRetroBlackIcons()
    window.show()
    sys.exit(app.exec())