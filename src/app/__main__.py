"""GUI Application Module Entrypoint."""
from __future__ import annotations

import sys

from PySide6.QtCore import QFile, QLocale, QTextStream, QTranslator
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication

from ._ui import resources_rc
from .MainWindow import MainWindow

assert resources_rc, "We need this module to have been generated"


def main():
    """Main function."""
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":/icons/app.svg"))

    QFontDatabase.addApplicationFont(":/fonts/Roboto-Regular.ttf")
    app.setFont(QFont("Roboto"))

    f = QFile(":/style.qss")
    f.open(QFile.ReadOnly | QFile.Text)  # type: ignore[attr-defined]
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    translator.load(":/translations/" + QLocale.system().name() + ".qm")
    app.installTranslator(translator)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
