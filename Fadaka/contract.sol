// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FadakaBatchSender {

    function batchTransfer(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external payable {

        require(recipients.length == amounts.length, "Mismatch");

        uint256 total = 0;

        // Calculate total required
        for (uint i = 0; i < amounts.length; i++) {
            total += amounts[i];
        }

        require(msg.value >= total, "Insufficient funds");

        // Send funds
        for (uint i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(amounts[i]);
        }

        // Return change (like Bitcoin)
        if (msg.value > total) {
            payable(msg.sender).transfer(msg.value - total);
        }
    }
}
