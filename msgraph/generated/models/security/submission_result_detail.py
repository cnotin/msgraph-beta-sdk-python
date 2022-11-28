from enum import Enum

class SubmissionResultDetail(Enum):
    None_escaped = "none",
    UnderInvestigation = "underInvestigation",
    SimulatedThreat = "simulatedThreat",
    AllowedBySecOps = "allowedBySecOps",
    AllowedByThirdPartyFilters = "allowedByThirdPartyFilters",
    MessageNotFound = "messageNotFound",
    UrlFileShouldNotBeBlocked = "urlFileShouldNotBeBlocked",
    UrlFileShouldBeBlocked = "urlFileShouldBeBlocked",
    UrlFileCannotMakeDecision = "urlFileCannotMakeDecision",
    DomainImpersonation = "domainImpersonation",
    UserImpersonation = "userImpersonation",
    BrandImpersonation = "brandImpersonation",
    OutboundShouldNotBeBlocked = "outboundShouldNotBeBlocked",
    OutboundShouldBeBlocked = "outboundShouldBeBlocked",
    OutboundBulk = "outboundBulk",
    OutboundCannotMakeDecision = "outboundCannotMakeDecision",
    OutboundNotRescanned = "outboundNotRescanned",
    ZeroHourAutoPurgeAllowed = "zeroHourAutoPurgeAllowed",
    ZeroHourAutoPurgeBlocked = "zeroHourAutoPurgeBlocked",
    ZeroHourAutoPurgeQuarantineReleased = "zeroHourAutoPurgeQuarantineReleased",
    OnPremisesSkip = "onPremisesSkip",
    AllowedByTenantAllowBlockList = "allowedByTenantAllowBlockList",
    BlockedByTenantAllowBlockList = "blockedByTenantAllowBlockList",
    AllowedUrlByTenantAllowBlockList = "allowedUrlByTenantAllowBlockList",
    AllowedFileByTenantAllowBlockList = "allowedFileByTenantAllowBlockList",
    AllowedSenderByTenantAllowBlockList = "allowedSenderByTenantAllowBlockList",
    AllowedRecipientByTenantAllowBlockList = "allowedRecipientByTenantAllowBlockList",
    BlockedUrlByTenantAllowBlockList = "blockedUrlByTenantAllowBlockList",
    BlockedFileByTenantAllowBlockList = "blockedFileByTenantAllowBlockList",
    BlockedSenderByTenantAllowBlockList = "blockedSenderByTenantAllowBlockList",
    BlockedRecipientByTenantAllowBlockList = "blockedRecipientByTenantAllowBlockList",
    AllowedByConnection = "allowedByConnection",
    BlockedByConnection = "blockedByConnection",
    AllowedByExchangeTransportRule = "allowedByExchangeTransportRule",
    BlockedByExchangeTransportRule = "blockedByExchangeTransportRule",
    QuarantineReleased = "quarantineReleased",
    QuarantineReleasedThenBlocked = "quarantineReleasedThenBlocked",
    JunkMailRuleDisabled = "junkMailRuleDisabled",
    AllowedByUserSetting = "allowedByUserSetting",
    BlockedByUserSetting = "blockedByUserSetting",
    AllowedByTenant = "allowedByTenant",
    BlockedByTenant = "blockedByTenant",
    InvalidFalsePositive = "invalidFalsePositive",
    InvalidFalseNegative = "invalidFalseNegative",
    SpoofBlocked = "spoofBlocked",
    GoodReclassifiedAsBad = "goodReclassifiedAsBad",
    GoodReclassifiedAsBulk = "goodReclassifiedAsBulk",
    GoodReclassifiedAsGood = "goodReclassifiedAsGood",
    GoodReclassifiedAsCannotMakeDecision = "goodReclassifiedAsCannotMakeDecision",
    BadReclassifiedAsGood = "badReclassifiedAsGood",
    BadReclassifiedAsBulk = "badReclassifiedAsBulk",
    BadReclassifiedAsBad = "badReclassifiedAsBad",
    BadReclassifiedAsCannotMakeDecision = "badReclassifiedAsCannotMakeDecision",
    UnknownFutureValue = "unknownFutureValue",

