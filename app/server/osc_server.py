import argparse

from pythonosc import dispatcher
from pythonosc import osc_server

def print_joint(unused_addr, joint, user, x, y, z):
  print("{} {} {} {} {}".format(joint, user, x, y, z))


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="192.168.1.11", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=7110, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/joint", print_joint)

  server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
  # print("Serving on {}".format(server.server_address))
  server.serve_forever()