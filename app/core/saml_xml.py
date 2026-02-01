from datetime import datetime
from xml.etree import ElementTree as ET


def build_authn_request(
    issuer: str, acs_url: str, issue_instant: datetime
) -> str:
    root = ET.Element("AuthRequest")
    ET.SubElement(root, "Issuer").text = issuer
    ET.SubElement(root, "IssueInstant").text = issue_instant.isoformat()
    ET.SubElement(root, "AssertionConsumerServiceURL").text = acs_url

    return ET.tostring(root, encoding="unicode")


def parse_assertion(xml: str) -> dict[str, str]:
    root = ET.fromstring(xml)

    data = {
        "issuer": root.findtext("Issuer"),
        "subject": root.findtext("Subject"),
        "issued_at": root.findtext("IssuedAt"),
    }

    return data
