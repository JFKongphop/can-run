require("@nomiclabs/hardhat-waffle");

// Replace this private key with your Goerli account private key
// To export your private key from Metamask, open Metamask and
// go to Account Details > Export Private Key
// Be aware of NEVER putting real Ether into testing accounts

module.exports = {
  solidity: "0.8.1",
  networks: {
    arbitrum: {
      url: `https://rinkeby.arbitrum.io/rpc`, // can use any of testnet for deploy of contract
      accounts: [`your private key`]
    }
  }
};