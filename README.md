# Breed Enter

Provides a macOS and Linux available enter breed interface tool

## How it works

1. Every 500ms, Send `BREED:ABORT` to broadcast address, port 37541
1. Wait for port 37541 to reply with `BREED:ABORT` magic packet

## References

- <https://github.com/Izib/PHICOMM_openwrt>
- <https://www.right.com.cn/forum/thread-194833-1-1.html>

## LICENSE

[MIT LICENSE](LICENSE)