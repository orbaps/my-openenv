from fastapi import FastAPI
from server.environment import SimpleEnv

app = FastAPI()
env = SimpleEnv()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs,
        "reward": 0,
        "done": False
    }


@app.get("/reset")
def reset_get():
    return reset()


@app.post("/step")
def step(action: dict):
    obs, reward, done = env.step(action.get("action", "save"))
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return env.get_state()


def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
