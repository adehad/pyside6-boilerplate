"""MainWindow tests."""
from __future__ import annotations

from unittest import mock

from PySide6.QtCore import QCoreApplication
from pytestqt.qtbot import QtBot, qt_api

from app.MainWindow import MainWindow


def test_about_button(qtbot: QtBot):
    """Test the about button."""
    # GIVEN: the MainWindow
    widget = MainWindow()
    qtbot.addWidget(widget)

    assert widget.ui.about.click_count == 0
    # WHEN: we click the button
    with mock.patch(
        f"{QCoreApplication.__module__}.{QCoreApplication.__name__}.{QCoreApplication.instance.__name__}"
    ) as patch_qcore_instance:
        qtbot.mouseClick(
            widget.ui.about.ui.builtWithQtBtn, qt_api.QtCore.Qt.MouseButton.LeftButton
        )

    # THEN: the about window is shown
    assert (
        patch_qcore_instance.mock_calls[-1] == mock.call(patch_qcore_instance).aboutQt()
    )
    # THEN: the click count increments
    assert widget.ui.about.click_count == 1
