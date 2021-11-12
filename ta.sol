 /* @dev PURPOSE
 *
 Reggie the Random Oracle (not his real job) wants to provide randomness
 to Vera the verifier in such a way that Vera can be sure he's not
 making his output up to suit himself. Reggie provides Vera a public key
 to which he knows the secret key. Each time Vera provides a seed to
 Reggie, he gives back a value which is computed completely
 deterministically from the seed and the secret key.
 
 Reggie provides a proof by which Vera can verify that the output was
 correctly computed once Reggie tells it to her, but without that proof,
 the output is indistinguishable to her from a uniform random sample
 from the output space.
 
 The purpose of this contract is to make it easy for unrelated contracts
 to talk to Vera the verifier about the work Reggie is doing, to provide
 simple access to a verifiable source of randomness.
 
 
 
USAGE

Calling contracts must inherit from VRFConsumerBase, and can
initialize VRFConsumerBase's attributes in their constructor as
shown:

  contract VRFConsumer {
    constuctor(<other arguments>, address _vrfCoordinator, address _link)
      VRFConsumerBase(_vrfCoordinator, _link) public {
        <initialization with other arguments goes here>
      }
  }

The oracle will have given you an ID for the VRF keypair they have
committed to (let's call it keyHash), and have told you the minimum LINK
price for VRF service. Make sure your contract has sufficient LINK, and
call requestRandomness(keyHash, fee, seed), where seed is the input you
want to generate randomness from.

Once the VRFCoordinator has received and validated the oracle's response
to your request, it will call your contract's fulfillRandomness method.

The randomness argument to fulfillRandomness is the actual random value
generated from your seed.

The requestId argument is generated from the keyHash and the seed by
makeRequestId(keyHash, seed). If your contract could have concurrent
requests open, you can use the requestId to track which seed is
associated with which randomness. See VRFRequestIDBase.sol for more
details. (See "SECURITY CONSIDERATIONS" for principles to keep in mind,
if your contract could have multiple requests in flight simultaneously.)

Colliding `requestId`s are cryptographically impossible as long as seeds
differ. (Which is critical to making unpredictable randomness! See the
next section.)
 
 */