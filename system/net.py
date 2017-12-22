# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,R0913

"""Net Functions
The following functions give you access to interact with http services."""

__all__ = [
    'sendEmail'
]


def sendEmail(smtp, fromAddr, subject, body, html, to, priority='3'):
    """Sends an email through the given SMTP server. Note that this email is relayed first through
    the Gateway - the client host machine doesn't need network access to the SMTP server.

    Args:
        smtp (str): The address of an SMTP server to send the email through, like
            "mail.example.com". A port can be specified, like "mail.example.com:25". SSL can also
            be forced, like "mail.example.com:25:tls".
        fromAddr (str): An email address to have the email come from.
        subject (str): The subject line for the email
        body (str): The body text of the email.
        html (bool): A flag indicating whether or not to send the email as an HTML email. Will
            auto-detect if omitted.
        to (list[str]): A list of email addresses to send to.
        priority (str): Priority for the message, from "1" to "5", with "1" being highest priority.
            Defaults to "3" (normal) priority.
    """
    print(smtp, fromAddr, subject, body, html, to, priority)
