from enum import Enum

class EdgeOpenOptions(Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # StartPage.
    StartPage = "startPage",
    # NewTabPage.
    NewTabPage = "newTabPage",
    # PreviousPages.
    PreviousPages = "previousPages",
    # SpecificPages.
    SpecificPages = "specificPages",

