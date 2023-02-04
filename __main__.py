import sys

from spotify_request import SpotifyRequest

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    req = SpotifyRequest()
    req.run_requests()

if __name__ == '__main__':
    sys.exit(main())