"""MainWindow."""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QLabel, QMainWindow

from app._ui.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Main Window."""
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        hello = self.__tr("Hello, click the logo for information about Qt")
        clickQt = QLabel(self)
        # clickQt.setWordWrap(True)
        clickQt.setText(hello)
        self.ui.verticalLayout.insertWidget(0, clickQt)
        # self.adjustSize()

    def __tr(self, txt: str, disambiguation: None | str = None, n=-1) -> str:
        """Custom Translation function.

        Needed for https://bugreports.qt.io/browse/PYSIDE-131
        Resolved in Qt6, but it could be a tiny bit faster than tr()
        """
        context = ""  # For some reason, translation files don't use filename as context
        return QCoreApplication.translate(context, txt, disambiguation, n)
