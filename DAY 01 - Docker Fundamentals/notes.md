# The Traditional Way 

- The code passes in Dev — because the developer just wrote it and tested it locally.

- It passes again in Test — because that environment happens to be similar enough. So everyone assumes it's ready.

- Then it gets handed to Ops for the real deployment, and it fails in Production.

- Why?

  - Because Dev, Test, and Prod aren't identical.
  
  - Maybe Prod has different environment variables, due to misconfiguration and misalignments, a different OS version, missing dependencies, or scaled-up traffic that exposes a bug the smaller test environment never hit.
  
  - The developer's classic (and slightly infamous) line at this point is: **"but it works on my machine."**

- This is exactly the problem **containers solve** — package the app with everything it needs (dependencies, config, runtime, binaries, application and Operating System) into one image, and that same image runs identically in Dev, Test, and Prod.

- No more environment drift, no more "works on my machine."
