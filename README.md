# Review Counter

Look through merged PRs and look for some value like LGTM or :+1: and
credit that person with reviewing it.

## Usage

```bash
python main.py \
    --token=$TOKEN \
    --since 2016-1-1 \
    --repo=mitodl/ccxcon \
    --repo=mitodl/teachersportal \
    --repo=mitocw/edx-platform \
    --repo=mitodl/lore
```

`$TOKEN` is a personal access token which has access to `public_repo`
and `repo` permissions. You can generate those
[here](https://github.com/settings/tokens).
