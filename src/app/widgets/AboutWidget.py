"""About Widget."""
from __future__ import annotations

from PySide6.QtCore import QCoreApplication, qVersion
from PySide6.QtWidgets import QApplication, QWidget

import app
from app._ui.AboutWidget_ui import Ui_AboutWidget


class AboutWidget(QWidget):
    """About Widget."""

    def __init__(self, parent=None):
        """About Widget."""
        super().__init__(parent)
        self.ui = Ui_AboutWidget()
        self.ui.setupUi(self)

        self.ui.version.setText(app.__version__)
        self.ui.qtVersion.setText(qVersion())

        self.click_count = 0
        self.ui.builtWithQtBtn.clicked.connect(self.open_about_dialog)

    def open_about_dialog(self):
        """Opens the About dialog."""
        core_app = QApplication.instance()
        if isinstance(core_app, QCoreApplication):
            core_app.aboutQt()  # type: ignore[attr-defined]
        self.click_count += 1
