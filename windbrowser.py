import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class WindBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # --- Pencere Ayarları ---
        self.setWindowTitle('WindBrowser // Core V7')
        self.setGeometry(100, 100, 1200, 800)
        
        # --- Karanlık Tema (WindOS Fütüristik Tarzı) ---
        self.setStyleSheet("""
            QMainWindow { background-color: #1E2124; }
            QToolBar { background-color: #282B30; border: none; padding: 5px; }
            QPushButton { 
                color: #DCDDDE; 
                background-color: #424549; 
                border-radius: 5px; 
                padding: 5px 15px; 
                font-weight: bold; 
            }
            QPushButton:hover { background-color: #7289DA; }
            QLineEdit { 
                background-color: #1E2124; 
                color: #DCDDDE; 
                border: 1px solid #424549; 
                border-radius: 8px; 
                padding: 5px 15px; 
                font-size: 14px; 
            }
            QLineEdit:focus { border: 1px solid #7289DA; }
        """)

        # --- Tarayıcı Motoru (Chromium Tabanlı) ---
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # --- Üst Araç Çubuğu (Navbar) ---
        navbar = QToolBar()
        navbar.setMovable(False)
        self.addToolBar(navbar)

        # Geri Butonu
        back_btn = QPushButton("◀ Geri")
        back_btn.clicked.connect(self.browser.back)
        navbar.addWidget(back_btn)

        # İleri Butonu
        forward_btn = QPushButton("İleri ▶")
        forward_btn.clicked.connect(self.browser.forward)
        navbar.addWidget(forward_btn)

        # Yenile Butonu
        reload_btn = QPushButton("⟳ Yenile")
        reload_btn.clicked.connect(self.browser.reload)
        navbar.addWidget(reload_btn)

        # Adres Çubuğu
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Web'de ara veya URL girin...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # URL değiştiğinde adres çubuğunu otomatik güncelle
        self.browser.urlChanged.connect(self.update_url)

    # --- Yönlendirme ve Arama Motoru Mantığı ---
    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        
        # Eğer site adresi yazıldıysa (örn: wind-os.com)
        if "." in url and " " not in url:
            if not url.startswith("http"):
                url = "https://" + url
        # Sadece kelime yazıldıysa Google'da ara
        else:
            url = "https://www.google.com/search?q=" + url.replace(" ", "+")
        
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindBrowser()
    window.show()
    sys.exit(app.exec_())
