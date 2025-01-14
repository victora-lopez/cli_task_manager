#! /usr/bin/python3
import argparse

def main():
    parser = argparse.ArgumentParser(prog='task-cli',
                                     description='A cli command that helps organize tasks with add, update, complete, and delete commands.')
    parser.add_argument('command',
                        type=str,
                        help='The command used to add,update,complete, or delete a task',
                        choices=['add','update','delete','mark-in-progress','mark-done','list'])
    args = parser.parse_args()

if __name__ == '__main__':
    main()
