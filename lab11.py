# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline:
    #   1. One coroutine per number that returns n * 2
    #   2. Run them all CONCURRENTLY with asyncio.gather(*coros)
    #   3. gather preserves input order, so return the results as a list
    async def double(n):
        return n * 2

    coros = [double(n) for n in numbers]
    results = await asyncio.gather(*coros)
    return list(results)


async def fastest(jobs):
    # Outline:
    #   1. One coroutine per (label, delay): await asyncio.sleep(delay); return label
    #   2. Start them all concurrently with asyncio.as_completed(coros)
    #   3. The first result yielded is the winner -> return its label
    async def run_job(label, delay):
        await asyncio.sleep(delay)
        return label

    coros = [run_job(label, delay) for label, delay in jobs]
    for coro in asyncio.as_completed(coros):
        return await coro


def echo_once(host, port, message):
    # Outline:
    #   1. Create a TCP socket (AF_INET, SOCK_STREAM)
    #   2. Connect to (host, port)
    #   3. sendall(message.encode())
    #   4. data = recv(1024); return data.decode()
    #   5. Use `with` so the socket is always closed
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode())
        data = sock.recv(1024)
        return data.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()