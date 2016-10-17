import logging as log
from logging.handlers import TimedRotatingFileHandler


class EvilEyeFormatter(log.Formatter):

    err_fmt = "[!] %(msg)s"
    # dbg_fmt = "[D] %(module)s: %(lineno)d: %(msg)s"
    dbg_fmt = "[D] %(msg)s"
    inf_fmt = "[+] %(msg)s"
    wrn_fmt = "[-] %(msg)s"

    def __init__(self, fmt="%(levelno)s: %(msg)s"):
        log.Formatter.__init__(self, fmt)

    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._fmt

        # Replace the original format with one customized by log level
        if record.levelno == log.DEBUG:
            self._fmt = self.dbg_fmt
        elif record.levelno == log.INFO:
            self._fmt = self.inf_fmt
        elif record.levelno == log.WARNING:
            self._fmt = self.wrn_fmt
        elif record.levelno == log.ERROR:
            self._fmt = self.err_fmt

        # Call the original formatter class to do the grunt work
        result = log.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._fmt = format_orig

        return result
