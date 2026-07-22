# Liveness Health Probe with command probe type Demo 

---

Step 1 :  liveness Yaml file 

---

<img width="1824" height="737" alt="image" src="https://github.com/user-attachments/assets/7f944ffc-621f-4344-8924-b8d17d8250e5" />


---

How this yaml file exceute : 

## What the container does

```
touch /tmp/healthy; sleep 30; rm -f /tmp/healthy; sleep 600
```

This is a shell script run as the container's main process:

| Step | Action | Duration |
|---|---|---|
| 1 | `touch /tmp/healthy` | Creates the file immediately |
| 2 | `sleep 30` | File exists for 30 seconds |
| 3 | `rm -f /tmp/healthy` | Deletes the file |
| 4 | `sleep 600` | File stays gone for next 10 minutes |

So the container is **deliberately designed to become "unhealthy" after 30 seconds** — this is a test/demo pattern to let you watch a liveness failure happen on purpose.

## What the probe does

```yaml
livenessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```

- **Mechanism:** `exec` — kubelet runs `cat /tmp/healthy` *inside the container* on a schedule.
- **Success condition:** exit code `0` → file exists → `cat` succeeds → probe passes.
- **Failure condition:** file doesn't exist → `cat` errors out → non-zero exit code → probe fails.
- `initialDelaySeconds: 5` → kubelet waits 5s after container start before the first check.
- `periodSeconds: 5` → checks every 5s after that.
- `failureThreshold` isn't set here → defaults to **3**. So it takes 3 consecutive failures before kubelet acts.

## Timeline of what actually happens

| Time | File state | Probe result |
|---|---|---|
| 0s | container starts, file created immediately | — |
| 5s | first probe runs | file exists → pass |
| 10s, 15s, 20s, 25s | probes run | file exists → pass |
| 30s | file gets deleted | — |
| 30s–35s | file missing | next probe (~30-35s) → **fail #1** |
| ~35-40s | still missing | **fail #2** |
| ~40-45s | still missing | **fail #3** → threshold hit |
| ~45s | kubelet kills and restarts the container | RESTARTS count → 1 |

After restart, the whole cycle repeats — file created again, healthy for 30s, fails again, restarts again. So if you leave this pod running, you'll see it restart roughly every ~75-80 seconds in a loop.

---

Step 2 : Apply and create the prob 

---

<img width="766" height="55" alt="image" src="https://github.com/user-attachments/assets/484984b2-36c1-4e35-b542-f72c4788a281" />


---

Step 3 : Check pod status - it will restart because we have specify the commands like that 

---

<img width="857" height="81" alt="image" src="https://github.com/user-attachments/assets/58464786-1402-4c08-ae23-b3dfa0ecd78d" />

---

Step 4 : Check after some seconds - the pod will be restarted 

---

<img width="924" height="86" alt="image" src="https://github.com/user-attachments/assets/50cc46b5-5e7e-4c65-ae77-b4db99f6345b" />

---

Step 5 : Check the events by describe commands 

---

<img width="1920" height="268" alt="image" src="https://github.com/user-attachments/assets/c7d477f2-0c85-40ce-8947-dfed8128626d" />


---

