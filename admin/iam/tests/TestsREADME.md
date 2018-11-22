# TESTING IAM

The are tests for the intern endpoint querys. You will find the gists files at `./querys` and `./mutations`.

These tests are located at https://gist.github.com/slucea 

Each gist file contains some querys that ensure that the result of the fucntion is as expected.

The tested querys are the following ones: 

Querys
- Organizations
	* List all orgs (callback)
	* List orgs with filter code (result)
- Products
	* List all products (callback)
	* List products with filter code (callback)
- Members
	* List all members (callback)
	* List members with filter code (result)
	* List members with filter type (callback)
- Groups
	* List all groups (callback)
	* List groups with filter code (result)
	* List groups with filter type (callback)
- Apis
	* List all apis (callback)
	* List apis with filter code (result)
- Resources
	* List all resources (callback)
	* List resources with filer code (result)
- Roles
	* List all roles (callback)
	* List roles with filter type (callback)
	* List roles with filter code (result)
- Pagination
	* List all pages with filters first/last after/before (callback)

 Mutations
- Organizations:
	* Create org 
	* List org with filter code
	* Delete org
	* List org with filer code
	* updateOrganizationDomain: ADD domain
	* List domain: check existance
	* updateOrganizationDomain: DEL domain
	* List domain: check non-existance
- Groups
	* Create group (callback)
	* List group with filter code (result)
	* Delete Groups (callback)
	* List group with filter code (result)
- Products
	* Create product (result)
	* Delete product (result)
- Resources
	* Create resource (result)
	* Delete resource (result)
- Members
	* Create member (result)
	* Update member (result)
	* Delete member (result)

## Execute tests

At  `graphql-schema/scripting/gateway` directory run:
 
```bash
$ py test_gateway --verbose --file=admin/iam/tests/querys/file.gist
```
or
```bash
$ py test_gateway --verbose --file=admin/iam/tests/mutations/file.gist
```

To know more about the gist files read the `graphql-schema/scripting/gateway/TestingGateway.md`