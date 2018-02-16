## 2018-01-30

⚠️  Input field `hotelCode` was added to input object type `HotelXHotelDataInput`

⚠️  Input field `supplierCode` was removed from input object type `HotelXHotelDataInput`

⚠️  Field `rsAccess` was removed from object type `StatAccess`

⚠️  Field `rqAccess` was removed from object type `StatAccess`

⚠️  Field `dockerID` was removed from object type `StatAccess`

⚠️  Field `dockerID` was removed from object type `StatPlugin`

⚠️  Field `rsPlugin` was removed from object type `StatsRequest`

⚠️  Field `rqPlugin` was removed from object type `StatsRequest`

⚠️  Field `rs` was removed from object type `StatsRequest`

⚠️  Field `rq` was removed from object type `StatsRequest`

⚠️  Field `config` was removed from object type `StatsRequest`

⚠️  Field `supplierCode` was removed from object type `HotelData`

✅  Description for enum value `BookStatusType.UNKNOWN` changed from `The status of the booking is unknown` to `The reservation was completed but due to a supplier error or a timeout, the reservation status is unknown. 

It is the client's responsibility to check if the booking is OK`

✅  Description for enum value `BookStatusType.ON_REQUEST` changed from `The status of the booking is on request` to `The reservation was completed but the product is still not available, so the reservation goes into a waiting list. 

It is the client's responsibility to check if the booking is OK`

✅  Description for enum value `BookStatusType.OK` changed from `The status of the booking is available` to `The reservation was completed with no problems`

✅  Field `StatTransaction.parseResponse` description changed from `` to `Parse response time`

✅  Field `StatTransaction.workerCommunication` description changed from `` to `Worker connection time`

✅  Field `StatTransaction.buildRequest` description changed from `` to `Build request time`

✅  Field `StatTransaction.total` description changed from `` to `Total transaction time`

✅  Field `StatTransaction.reference` description changed from `` to `Extra information about transaction.`

✅  Field `StatAccess.plugins` description changed from `` to `Plugin execution time`

✅  Field `StatAccess.transactions` description changed from `` to `Detail transaction time`

✅  Field `StatAccess.cities` description changed from `` to `Number of cities`

✅  Field `StatAccess.zones` description changed from `` to `Number of zones`

✅  Field `StatAccess.hotels` description changed from `` to `Number of hotels`

✅  Field `StatAccess.staticConfiguration` description changed from `` to `Static configuration time`

✅  Field `StatAccess.total` description changed from `` to `Total access time`

✅  Field `StatAccess.name` description changed from `` to `Access name`

✅  Field `responseAccess` was added to object type `StatAccess`

✅  Field `requestAccess` was added to object type `StatAccess`

✅  Field `StatPlugin.total` description changed from `` to `total plugin time`

✅  Field `StatPlugin.name` description changed from `` to `Plugin name`

✅  Field `StatsRequest.Accesses` description changed from `` to `Detail access time`

✅  Field `StatsRequest.dockerID` description changed from `` to `Docker Id`

✅  Field `StatsRequest.cities` description changed from `` to `Number of cities`

✅  Field `StatsRequest.zones` description changed from `` to `Number of zones`

✅  Field `StatsRequest.hotels` description changed from `` to `Number of hotels`

✅  Field `StatsRequest.process` description changed from `` to `Process time. Contains communication time, parse time and plugin time.`

✅  Field `StatsRequest.validation` description changed from `` to `Request validation time`

✅  Field `StatsRequest.total` description changed from `` to `Total transaction time`

✅  Field `responsePlugin` was added to object type `StatsRequest`

✅  Field `requestPlugin` was added to object type `StatsRequest`

✅  Field `response` was added to object type `StatsRequest`

✅  Field `request` was added to object type `StatsRequest`

✅  Field `configuration` was added to object type `StatsRequest`

✅  Field `hotelCode` was added to object type `HotelData`

## 2018-01-29

⚠️  Field `HotelCancelPayload.stats` changed type from `RequestStats` to `StatsRequest`

⚠️  Field `HotelBookPayload.stats` changed type from `RequestStats` to `StatsRequest`

⚠️  Input field `supplierCode` was added to input object type `HotelXHotelDataInput`

⚠️  Input field `code` was removed from input object type `HotelXHotelDataInput`

⚠️  Type for argument `relay` on field `HotelXMutation.updateHotel` changed from `HotelXRelayInput` to `RelayInput`

⚠️  Field `HotelBooking.stats` changed type from `RequestStats` to `StatsRequest`

⚠️  Field `HotelQuote.stats` changed type from `RequestStats` to `StatsRequest`

⚠️  Field `external` was removed from object type `StatAccess`

⚠️  Field `Response.stats` changed type from `RequestStats` to `StatsRequest`

⚠️  Field `HotelSearch.stats` changed type from `RequestStats` to `StatsRequest`

⚠️  Input field `codes` was removed from input object type `HotelXHotelQueryInput`

⚠️  Type for argument `language` on field `HotelData.generalDescription` changed from `Language` to `String`

⚠️  Type for argument `language` on field `HotelData.additionalInformation` changed from `Language` to `String`

⚠️  Type for argument `language` on field `HotelData.amenities` changed from `Language` to `String`


⚠️  Type for argument `relay` on field `HotelXQuery.hotels` changed from `HotelXRelayInput` to `RelayInput`

⚠️  `RequestStats` was removed

⚠️  `HotelXRelayInput` was removed

✅  Input field `supplierGroup` was added to input object type `SupplierInput`

✅  Input field `serviceAPI` was added to input object type `SupplierFilter`

✅  Input field `isActive` was added to input object type `SupplierFilter`

✅  Field `supplierGroup` was added to object type `SupplierData`

✅  Description `Url's` on type `UrlsInput` has changed to `Url's Input`

✅  Field `plugins` was added to object type `StatAccess`

✅  Field `rsAccess` was added to object type `StatAccess`

✅  Field `rqAccess` was added to object type `StatAccess`

✅  Field `dockerID` was added to object type `StatAccess`

✅  Field `cities` was added to object type `StatAccess`

✅  Field `zones` was added to object type `StatAccess`

✅  Field `hotels` was added to object type `StatAccess`

✅  Input field `supplierCodes` was added to input object type `HotelXHotelQueryInput`

✅  Field `HotelData.code` description changed from `Internal code to perform availability and/or supplier code.` to `Internal code to perform availability`

✅  Field `supplierCode` was added to object type `HotelData`

✅  Type `StatPlugin` was added

✅  Type `StatsRequest` was added

✅  Type `RelayInput` was added

## 2018-01-17

⚠️  Field `AccessEdge.node` changed type from `Supplier` to `Access`

⚠️  Field `value` was removed from object type `Parameter`

⚠️  Field `key` was removed from object type `Parameter`

⚠️  Field `supplierGroups` was removed from object type `SupplierData`

⚠️  Field `hotelCodes` was removed from object type `SupplierData`

⚠️  Field `dll` was removed from object type `SupplierData`

⚠️  Field `Supplier.supplierData` changed type from `SupplierData!` to `SupplierData`

⚠️  Field `AccessData.parameters` changed type from `[Parameter!]` to `ParameterConnection`

⚠️  Field `AccessData.urls` changed type from `Urls!` to `Urls`

⚠️  Field `AccessData.supplier` changed type from `String!` to `Supplier!`

⚠️  Field `AccessData.code` changed type from `String!` to `ID!`

⚠️  Field `id` was removed from object type `AccessData`

⚠️  Field `suppliers` was removed from object type `AccessData`

⚠️  Field `Access.accessData` changed type from `AccessData!` to `AccessData`

✅  `Parameter` object implements `Node` interface

✅  Description `Parameters for additional information for the supplier's configuration.` on type `Parameter` has changed to ``

✅  Field `updatedAt` was added to object type `Parameter`

✅  Field `createdAt` was added to object type `Parameter`

✅  Field `error` was added to object type `Parameter`

✅  Field `parameterData` was added to object type `Parameter`

✅  Field `code` was added to object type `Parameter`

✅  Field `legacy` was added to object type `SupplierData`

✅  Field `serviceApi` was added to object type `SupplierData`

✅  Field `context` was added to object type `SupplierData`

✅  Field `provider` was added to object type `SupplierData`

✅  Field `name` was added to object type `SupplierData`

✅  Argument `after: String` added to field `AccessData.parameters`

✅  Argument `before: String` added to field `AccessData.parameters`

✅  Argument `Last: Int` added to field `AccessData.parameters`

✅  Argument `first: Int` added to field `AccessData.parameters`

✅  Field `AccessData.code` description changed from `Access code.` to `Unique AccessConfiguration identifier`

✅  Field `shared` was added to object type `AccessData`

✅  Field `rateRules` was added to object type `AccessData`

✅  Field `descriptiveInfoLimit` was added to object type `AccessData`

✅  Field `deleteSupplierFromGroup` was added to object type `AdminMutation`

✅  Field `grantSupplierToGroup` was added to object type `AdminMutation`

✅  Field `deleteAccessFromGroup` was added to object type `AdminMutation`

✅  Field `grantAccessToGroup` was added to object type `AdminMutation`

✅  Field `updateAccess` was added to object type `AdminMutation`

✅  Field `createAccess` was added to object type `AdminMutation`

✅  Input field `RankInput.rank4` changed type from `Boolean!` to `Boolean`

✅  Input field `RankInput.rank3` changed type from `Boolean!` to `Boolean`

✅  Input field `RankInput.rank2` changed type from `Boolean!` to `Boolean`

✅  Input field `RankInput.rank1` changed type from `Boolean!` to `Boolean`

✅  Field `suppliers` was added to object type `AdminQuery`

✅  Field `accesses` was added to object type `AdminQuery`

✅  Field `CancelPolicy.refundable` description changed from `Indicates if the option is refundable or not.
This information is mandatory.` to `Indicates if the option is refundable or not.`

✅  Input field `ranks` was added to input object type `HotelXHotelQueryInput`

✅  Type `SupplierInput` was added

✅  Type `ProviderInput` was added

✅  Type `LegacyDataInput` was added

✅  Type `Context` was added

✅  Type `GroupInput` was added

✅  Type `AccessInput` was added

✅  Type `SupplierFilter` was added

✅  Type `SupplierEdge` was added

✅  Type `SupplierConnection` was added

✅  Type `AccessFilter` was added

✅  Type `ParameterData` was added

✅  Type `ParameterEdge` was added

✅  Type `ParameterConnection` was added

✅  Type `LegacyData` was added

✅  Type `Provider` was added

## 2018-01-11

⚠️  Field `codes` was removed from object type `Map`

⚠️  Field `supplierCode` was removed from object type `Map`

⚠️  Field `maps` was removed from object type `MappingEntity`

⚠️  Argument `BoardCodes: [String!]` was removed from field `MappingContext.boards`

⚠️  Argument `roomCodes: [String!]` was removed from field `MappingContext.rooms`

⚠️  Argument `hotelCodes: [String!]` was removed from field `MappingContext.hotels`

⚠️  Field `rates` was removed from object type `MappingContext`

⚠️  Field `contextCode` was removed from object type `MappingContext`

⚠️  Argument `supplierCodes: [String!]` was removed from field `Mapping.contexts`

⚠️  Argument `contextCodes: [String!]` was removed from field `Mapping.contexts`

⚠️  Field `DefaultSettings.market` changed type from `String!` to `String`

⚠️  Field `DefaultSettings.connectUser` changed type from `String!` to `String`

⚠️  Input field `HotelSettingsInput.suppliers` changed type from `[SupplierInput!]` to `[HotelXSupplierInput!]`

⚠️  Field `HotelSearch.requestCriteria` changed type from `CriteriaSearch!` to `CriteriaSearch`

⚠️  Field `HotelSearch.context` changed type from `String!` to `String`

⚠️  Field `Geocode.longitude` changed type from `String!` to `Float!`

⚠️  Field `Geocode.latitude` changed type from `String!` to `Float!`

⚠️  Argument `after: String` was removed from field `HotelXQuery.hotels`

⚠️  Argument `before: String` was removed from field `HotelXQuery.hotels`

⚠️  Argument `last: Int` was removed from field `HotelXQuery.hotels`

⚠️  Argument `first: Int` was removed from field `HotelXQuery.hotels`

⚠️  Argument `language: String` was removed from field `HotelXQuery.hotels`

⚠️  Argument `codes: [String!]` was removed from field `HotelXQuery.hotels`

⚠️  `HotelInput` was removed

⚠️  `AccessInput` was removed

⚠️  `SupplierInput` was removed

✅  Field `loadFile` was added to object type `HotelXMutation`

✅  Field `updateHotel` was added to object type `HotelXMutation`

✅  Field `maps` was added to object type `Map`

✅  Field `code` was added to object type `Map`

✅  Field `contexts` was added to object type `MappingEntity`

✅  Argument `codes: [String!]` added to field `MappingContext.boards`

✅  Field `MappingContext.boards` description changed from `Mapping of boards. Filter by board code.` to `Mapping of boards, you can filter by board code.`

✅  Argument `codes: [String!]` added to field `MappingContext.rooms`
✅  Field `MappingContext.rooms` description changed from `Mapping of rooms. Filter by room code.` to `Mapping of rooms, you can filter by room code.`

✅  Argument `codes: [String!]` added to field `MappingContext.hotels`
✅  Field `MappingContext.hotels` description changed from `Mapping of hotels. Filter by hotel code.` to `Mapping of hotels, you can filter by hotel code.`

✅  Field `code` was added to object type `MappingContext`

✅  Argument `codes: [String!]` added to field `Mapping.contexts`

✅  Field `warnings` was added to object type `Mapping`

✅  Field `errors` was added to object type `Mapping`

✅  Argument `type: GroupType` added to field `AdminQuery.groups`

✅  Argument `type: MemberType` added to field `AdminQuery.members`

✅  Field `rank` was added to object type `HotelData`

✅  Argument `relay: HotelXRelayInput` added to field `HotelXQuery.hotels`

✅  Argument `hotels: HotelXHotelQueryInput` added to field `HotelXQuery.hotels`

✅  Field `mapping` was added to object type `HotelXQuery`

✅  Type `StatusResponse` was added

✅  Type `HotelStatus` was added

✅  Type `RankInput` was added

✅  Type `HotelXHotelDataInput` was added

✅  Type `HotelXHotelMutationInput` was added

✅  Type `HotelXAccessInput` was added

✅  Type `HotelXSupplierInput` was added

✅  Type `HotelXRelayInput` was added

✅  Type `HotelXHotelQueryInput` was added

✅  Type `Rank` was added
