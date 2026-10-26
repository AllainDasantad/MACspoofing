# MACspoofing

A Python-based Linux networking tool for inspecting network interfaces, validating MAC addresses, and experimenting with MAC address spoofing in an authorized lab environment.

> **Project status:** In development

## Overview

A Media Access Control (MAC) address is a link-layer identifier associated with a network interface. MAC address spoofing changes the address presented by an interface to the network.

**MACspoofing** is a hands-on cybersecurity project designed to explore Linux networking, Python automation, and network interface management.

The project aims to provide a simple command-line interface for inspecting network interfaces and safely experimenting with MAC address changes on systems you own or are authorized to test.

## Planned Features

- [x] Detect available network interfaces.
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
- **Git and GitHub** — version control and project hosting
- **pytest** — planned automated testing framework

## Getting Started

### Prerequisites

- A Linux system with a supported network interface
- Python 3
- Git
- The `ip` command from iproute2
- Administrator privileges for operations that modify network interfaces

### Installation

Clone the repository:

```bash
git clone https://github.com/AllainDasantad/MACspoofing.git
cd MACspoofing
```

Check your Python installation:

```bash
python3 --version
```

Inspect available network interfaces:

```bash
ip link show
```

### Usage

Usage instructions will be added as the command-line interface is implemented.

Before modifying a network interface, ensure you have permission to administer the device and understand how to restore its previous configuration.

## Security and Safety

This project is intended for educational purposes and authorized security testing.

- Only use the tool on devices and networks you own or have permission to test.
- Changing a MAC address may temporarily interrupt network connectivity.
- MAC address spoofing does not guarantee anonymity or conceal your identity from every network.
- Network access controls and operating-system behavior may affect whether an address change succeeds.
- Privileged operations should use validated input and avoid unsafe shell-command construction.

## Testing

Automated tests will be added as the project develops.

The test suite will focus on:

- MAC address validation
- Invalid input handling
- Network interface parsing
- Error handling
- Mocked system commands
- Verification of spoofing and restoration workflows

Tests should not modify real network interfaces unless explicitly configured for an authorized test environment.

## Project Structure

The planned structure is:

```text
MACspoofing/
├── src/
│   └── macspoofing/
│       ├── __init__.py
│       ├── interfaces.py
│       ├── validator.py
│       └── spoof.py
├── tests/
│   ├── test_validator.py
│   └── test_interfaces.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

The structure may change as the implementation evolves.

## Learning Objectives

This project is an opportunity to develop practical skills in:

- Python scripting and modular programming
- Linux networking and network interface management
- Input validation and error handling
- Operating-system permissions and subprocess security
- Automated testing and debugging
- Git version control and technical documentation

## Roadmap

**Phase 1 — Network Discovery**

- Enumerate network interfaces.
- Read and display their MAC addresses.

**Phase 2 — Validation**

- Validate MAC address formatting.
- Reject malformed input.

**Phase 3 — MAC Address Management**

- Implement controlled MAC address changes.
- Verify changes and support restoration.

**Phase 4 — Reliability**

- Add logging, automated tests, and error handling.

**Phase 5 — Documentation**

- Add usage examples, terminal demonstrations, and verified test results.

## Disclaimer

This project is intended for learning about networking and cybersecurity. The author does not encourage unauthorized access, evasion of network security policies, or misuse of network identifiers.

Users are responsible for complying with applicable laws, network policies, and authorization requirements.

## Author
