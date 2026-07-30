from backend.app.runtime import RuntimeFactory

runtime = RuntimeFactory.create("huggingface")

print("Runtime created:")
print(type(runtime))

print("Loading model...")

runtime.load()

print("Model loaded")

print("Model device:")
print(next(runtime.model.parameters()).device)

runtime.unload()

print("Model unloaded")
