# Migrate customer responses to version 2

Update consumer response models and display logic from `name` to `full_name`, then select the `/v2` base URL. Keep the `id` field unchanged.

Test successful parsing, missing required fields, and HTTP 404. The consumer demo intentionally retains its v1 model so contract analysis has an affected integration to find.
