from asyncio import sleep, get_event_loop, DatagramProtocol
from socket import socket, AF_INET, SOCK_DGRAM

PORT = 37541
MAGIC_STRING = 'BREED:ABORT'


async def send_abort_boot_packet():
    conn = socket(AF_INET, SOCK_DGRAM)

    def send_magic_packet():
        conn.sendto(MAGIC_STRING.encode(), ('255.255.255.255', PORT))

    while True:
        await sleep(0.5)  # every 500ms send magic packet
        send_magic_packet()


class BreedEnterProtocol(DatagramProtocol):
    def datagram_received(self, data, addr):
        host, port = addr
        if data.decode() == MAGIC_STRING:
            # noinspection HttpUrlsUsage
            print("http://%s" % host)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(loop.create_datagram_endpoint(
        BreedEnterProtocol,
        local_addr=('0.0.0.0', PORT)
    ))
    loop.run_until_complete(send_abort_boot_packet())
    loop.run_forever()
