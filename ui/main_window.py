from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QStackedWidget,
    QGridLayout,
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("دستیار مالی شخصی")
        self.resize(1250, 780)

        self.setLayoutDirection(Qt.RightToLeft)

        self.apply_style()
        self.create_ui()

    # =========================
    # ظاهر برنامه
    # =========================

    def apply_style(self):

        self.setStyleSheet("""
            QWidget {
                font-family: "Segoe UI";
                font-size: 14px;
            }

            QMainWindow {
                background-color: #f5f6fa;
            }

            QFrame#sidebar {
                background-color: #1f2937;
            }

            QLabel#appTitle {
                color: white;
                font-size: 20px;
                font-weight: bold;
            }

            QPushButton#menuButton {
                background-color: transparent;
                color: #e5e7eb;
                border: none;
                padding: 12px;
                text-align: right;
                border-radius: 8px;
            }

            QPushButton#menuButton:hover {
                background-color: #374151;
            }

            QLabel#pageTitle {
                font-size: 26px;
                font-weight: bold;
                color: #111827;
            }

            QFrame#card {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
            }

            QLabel#cardTitle {
                color: #6b7280;
                font-size: 13px;
            }

            QLabel#cardValue {
                color: #111827;
                font-size: 22px;
                font-weight: bold;
            }

            QFrame#panel {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
            }

            QLabel#panelTitle {
                font-size: 17px;
                font-weight: bold;
                color: #111827;
            }

            QLabel#transaction {
                padding: 10px;
                border-bottom: 1px solid #eeeeee;
            }
        """)

    # =========================
    # ساخت رابط
    # =========================

    def create_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # -------------------------
        # Sidebar
        # -------------------------

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(230)

        sidebar_layout = QVBoxLayout(sidebar)

        sidebar_layout.setContentsMargins(15, 25, 15, 20)

        title = QLabel("💰 دستیار مالی")
        title.setObjectName("appTitle")
        title.setAlignment(Qt.AlignCenter)

        sidebar_layout.addWidget(title)
        sidebar_layout.addSpacing(30)

        buttons = [
            ("🏠  داشبورد", 0),
            ("💵  درآمدها", 1),
            ("💳  هزینه‌ها", 2),
            ("🏦  دارایی‌ها", 3),
            ("📉  بدهی‌ها", 4),
            ("🎯  اهداف مالی", 5),
            ("📊  گزارش‌ها", 6),
        ]

        for text, index in buttons:

            button = QPushButton(text)

            button.setObjectName("menuButton")
            button.setMinimumHeight(45)

            button.clicked.connect(
                lambda checked=False, i=index:
                self.change_page(i)
            )

            sidebar_layout.addWidget(button)

        sidebar_layout.addStretch()

        settings = QPushButton("⚙️  تنظیمات")
        settings.setObjectName("menuButton")
        settings.setMinimumHeight(45)

        sidebar_layout.addWidget(settings)

        # -------------------------
        # Pages
        # -------------------------

        self.pages = QStackedWidget()

        self.pages.addWidget(
            self.dashboard_page()
        )

        self.pages.addWidget(
            self.simple_page("💵 درآمدها")
        )

        self.pages.addWidget(
            self.simple_page("💳 هزینه‌ها")
        )

        self.pages.addWidget(
            self.simple_page("🏦 دارایی‌ها")
        )

        self.pages.addWidget(
            self.simple_page("📉 بدهی‌ها")
        )

        self.pages.addWidget(
            self.simple_page("🎯 اهداف مالی")
        )

        self.pages.addWidget(
            self.simple_page("📊 گزارش‌ها")
        )

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.pages)

    # =========================
    # Dashboard
    # =========================

    def dashboard_page(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setContentsMargins(
            35, 30, 35, 30
        )

        # عنوان

        title = QLabel("داشبورد مالی")
        title.setObjectName("pageTitle")

        layout.addWidget(title)

        layout.addSpacing(25)

        # -------------------------
        # کارت‌ها
        # -------------------------

        cards_layout = QGridLayout()

        cards_layout.setSpacing(15)

        cards = [
            ("💰 دارایی کل", "۰ تومان"),
            ("📉 بدهی کل", "۰ تومان"),
            ("💎 ثروت خالص", "۰ تومان"),
            ("💵 درآمد این ماه", "۰ تومان"),
        ]

        for index, (title_text, value) in enumerate(cards):

            card = QFrame()
            card.setObjectName("card")

            card_layout = QVBoxLayout(card)

            card_layout.setContentsMargins(
                20, 18, 20, 18
            )

            title_label = QLabel(title_text)
            title_label.setObjectName("cardTitle")

            value_label = QLabel(value)
            value_label.setObjectName("cardValue")

            value_label.setAlignment(
                Qt.AlignRight
            )

            card_layout.addWidget(title_label)
            card_layout.addSpacing(8)
            card_layout.addWidget(value_label)

            cards_layout.addWidget(
                card,
                0,
                index
            )

        layout.addLayout(cards_layout)

        layout.addSpacing(20)

        # -------------------------
        # پنل‌ها
        # -------------------------

        panels = QHBoxLayout()

        panels.setSpacing(15)

        # نمودار درآمد

        income_panel = QFrame()
        income_panel.setObjectName("panel")

        income_layout = QVBoxLayout(
            income_panel
        )

        income_title = QLabel(
            "📈 درآمد و هزینه"
        )

        income_title.setObjectName(
            "panelTitle"
        )

        income_layout.addWidget(
            income_title
        )

        income_info = QLabel(
            "\n\n\n"
            "نمودار در نسخه بعدی\n"
            "با اطلاعات واقعی نمایش داده می‌شود."
            "\n\n\n"
        )

        income_info.setAlignment(
            Qt.AlignCenter
        )

        income_layout.addWidget(
            income_info
        )

        # هزینه‌ها

        expense_panel = QFrame()
        expense_panel.setObjectName("panel")

        expense_layout = QVBoxLayout(
            expense_panel
        )

        expense_title = QLabel(
            "🥧 دسته‌بندی هزینه‌ها"
        )

        expense_title.setObjectName(
            "panelTitle"
        )

        expense_layout.addWidget(
            expense_title
        )

        expense_info = QLabel(
            "\n\n\n"
            "پس از ثبت هزینه‌ها\n"
            "تحلیل هزینه‌ها نمایش داده می‌شود."
            "\n\n\n"
        )

        expense_info.setAlignment(
            Qt.AlignCenter
        )

        expense_layout.addWidget(
            expense_info
        )

        panels.addWidget(
            income_panel
        )

        panels.addWidget(
            expense_panel
        )

        layout.addLayout(panels)

        layout.addSpacing(20)

        # -------------------------
        # تراکنش‌های اخیر
        # -------------------------

        transaction_panel = QFrame()
        transaction_panel.setObjectName(
            "panel"
        )

        transaction_layout = QVBoxLayout(
            transaction_panel
        )

        transaction_title = QLabel(
            "🧾 آخرین تراکنش‌ها"
        )

        transaction_title.setObjectName(
            "panelTitle"
        )

        transaction_layout.addWidget(
            transaction_title
        )

        transaction = QLabel(
            "هنوز تراکنشی ثبت نشده است."
        )

        transaction.setObjectName(
            "transaction"
        )

        transaction.setAlignment(
            Qt.AlignCenter
        )

        transaction_layout.addWidget(
            transaction
        )

        layout.addWidget(
            transaction_panel
        )

        layout.addStretch()

        return page

    # =========================
    # صفحات موقت
    # =========================

    def simple_page(self, title_text):

        page = QWidget()

        layout = QVBoxLayout(page)

        title = QLabel(title_text)

        title.setObjectName(
            "pageTitle"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(title)

        return page

    # =========================
    # تغییر صفحه
    # =========================

    def change_page(self, index):

        self.pages.setCurrentIndex(index)