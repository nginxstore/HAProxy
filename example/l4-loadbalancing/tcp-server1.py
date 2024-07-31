import socket

def start_server(host='0.0.0.0', port=65432):
    # TCP/IP 소켓 생성합니다.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 위에서 지정한 주소 및 포트를 설정합니다.
        s.bind((host, port))
        # 클라이언트 연결 대기합니다.
        s.listen()

        while True:
            # 클라이언트의 연결을 수락합니다.
            conn, addr = s.accept()
            with conn:
                # 클라이언트가 연결된 것을 확인하기 위해 콘솔로 ip를 출력합니다.
                print(f"{addr} connect")
                # 클라이언트에게 1을 전송합니다. 로드밸런싱을 확인하기 위해 각각 다른 메세지로 전송하였습니다.
                conn.sendall(b'1')


if __name__ == "__main__":
    start_server()



