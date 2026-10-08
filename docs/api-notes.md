# API exploration notes
Practice docket: FAA-2018-1084 (FAA rule on external markings for small drones)

## Documents endpoint
- Docket has 2 documents (`totalElements: 2`)
- FAA-2018-1084-0001: "Rule" (Interim Final Rule), comment period Feb 13 – Mar 16, 2019. This is the one people commented on.
- FAA-2018-1084-0002: "Supporting & Related Material" (a letter). `commentEndDate` is null, so no comments.
- `id` = readable ID (top level). `objectId` = internal ID (inside `attributes`). Use `objectId` to request comments.

## Comments list endpoint
- 418 comments on document 0001
- 25 per page by default (17 pages); max is 250 per page
- Each comment only has: id, postedDate, lastModifiedDate, withdrawn, title
- NO comment text in the list -> need 1 extra request per comment (418 here)
- Default order is not sorted by ID or date
- `title` looks like "Comment from [Name]"

## Single comment endpoint
- The actual text is in `attributes.comment`
- Text contains HTML: `<br/>` line breaks (sometimes shown as `\u003Cbr/\u003E`), `&quot;` for ", `&#39;` for ' -> needs cleaning before analysis
- Names: `firstName`, `lastName`. Anonymous commenters have both set to "Anonymous", not null
- city, stateProvinceRegion, country, zip, organization: null on both comments I checked
- Links back up: `commentOnDocumentId` (FAA-2018-1084-0001) and `docketId`
- Dates: `receiveDate` (agency received it) and `postedDate` (made public)
- Attachments: `relationships.attachments.data` is `[]` -> no attachments on either
- `duplicateComments: 0` -> not sure what this counts yet

## Questions / surprises
- A wrong filter returns everything instead of an error -> always check results match the request
- Location/organization fields are empty on this docket -> check these BEFORE choosing my real docket
- What does `duplicateComments` count? Could matter for form-letter detection