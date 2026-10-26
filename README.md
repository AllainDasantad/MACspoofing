# MACspoofing

A Python-based Linux networking tool for inspecting network interfaces, validating MAC addresses, and experimenting with MAC address spoofing in an authorized lab environment.

> **Project status:** In development

## Overview

A Media Access Control (MAC) address is a link-layer identifier associated with a network interface. MAC address spoofing changes the address presented by an interface to the network.

**MACspoofing** is a hands-on cybersecurity project designed to explore Linux networking, Python automation, and network interface management.

The project aims to provide a simple command-line interface for inspecting network interfaces and safely experimenting with MAC address changes on systems you own or are authorized to test.

## Planned Features

- [ ] Detect available network interfaces.
- [ ] Display current MAC addresses.
- [ ] Validate MAC address formats.
- [ ] Generate locally administered MAC addresses.
- [ ] Change a network interface's MAC address on supported Linux systems.
- [ ] Verify whether a requested address was applied.
- [ ] Restore the original interface configuration.
- [ ] Record operations and errors in an audit log.
- [ ] Include automated tests for core functionality.

*Features will be marked as complete as they are implemented and tested.*

## Technologies

- **Python 3** — core programming language
- **Linux** — target operating system
- **iproute2** — network interface inspection and management
- **Git and GitHub** — version
