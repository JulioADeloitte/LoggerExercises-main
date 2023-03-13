#maybe
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_logreport(report):
    yield

    # Define when you want to report:
    # when=setup/call/teardown,
    # fields: .failed/.passed/.skipped
    if report.when == 'teardown':
        # Add to the database or an issue tracker or wherever you want.
        print('\n')
        print(report.outcome)
        print(report.sections)
        print(report.duration)
        print(report.location)
        if report.user_properties:
            value = report.user_properties[0]
            print(value)
