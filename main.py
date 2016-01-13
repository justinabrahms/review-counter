import argparse
from datetime import datetime
import collections
from github import Github


def valid_date(s):
    """
    Convert argparse date into datetime.

    via http://stackoverflow.com/a/25470943/4972
    """
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{}'".format(s)
        raise argparse.ArgumentTypeError(msg)


def main(sentinel, repos, token, since):
    """
    Loop through merged prs in the available repos to find comments which
    contain sentinel values. Credit those users with reviewing it.
    """
    g = Github(token)
    to_check = set()
    for repo_str in repos:
        repo = g.get_repo(repo_str)
        for pr in repo.get_pulls(state='closed'):
            if pr.merged_at and pr.merged_at > since:
                to_check.add(pr)

    total_reviews = []
    for pr in to_check:
        for comment in pr.get_issue_comments():
            if sentinel in comment.body:
                total_reviews.append(comment.user.name)

    counter = collections.Counter(total_reviews)
    print '\n'.join(['%s: %s' % (x, y) for x,y in counter.most_common()])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count reviews on github")
    parser.add_argument('--sentinel', dest='sentinel', default=':+1:', help='String to look for to count something as "reviewed"')
    parser.add_argument('--repo', dest='repo', action='append', help="Repos to search through")
    parser.add_argument('--token', dest='token', help="Your github personal access token")
    parser.add_argument('--since', dest='since', type=valid_date, help="YYYY-MM-DD format of when to outer bound the request")

    args = parser.parse_args()

    if not args.repo:
        raise RuntimeError("You must specify one or more repos with --repo")
    if not args.since:
        raise RuntimeError("You must specify a valid time to start the check")

    main(args.sentinel, args.repo, args.token, args.since)
