# Review Counter

Look through merged PRs and look for some value like LGTM or :+1: and
credit that person with reviewing it.

## Usage

```bash
python main.py \
    --token $TOKEN \
    --since 2016-1-1 \
    --repos mitodl/ccxcon mitodl/teachersportal mitocw/edx-platform mitodl/lore \
    --sentinels :+1: :metal: :100:
```

`--sentinels`, optional, takes an unquoted, space-delimited list of strings, which, if any is matched in a search of the comments of a given repository, increments the commenter's total score.

`--repos`, required, takes a single string, or an unquoted, space-delimited list of strings, naming github code repositories in the form `<githubaccount>/<reponame>`, whose comments are to be scanned for those sentinel string values.

`$TOKEN` is a personal access token which has access to `public_repo`
and `repo` permissions. You can generate those
[here](https://github.com/settings/tokens).
