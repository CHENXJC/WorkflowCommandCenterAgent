from workflow_command.delivery_report import (
    build_demo_delivery_report,
    generate_delivery_report_markdown,
)


def test_delivery_report_generates_markdown():
    report = generate_delivery_report_markdown(build_demo_delivery_report())

    assert "# Delivery Report: WorkflowCommandCenterAgent" in report
    assert "Completed Items" in report
    assert "Modified Files" in report
    assert "Validation Results" in report
    assert "Next Recommended Action" in report
