## **🚀 Working with Python Layers for AWS Lambda Functions**

In AWS Lambda, **Layers** help manage libraries and other function dependencies separately from your main code. Layers are useful when you need to include large dependencies or when you want to reuse dependencies across multiple functions.

### **📂 Directory Structure for Python Modules**
When creating Python Lambda functions, the typical directory structure for Python modules within a layer is as follows:
```
layer_content.zip
└ python
    └ lib
        └ python3.11
            └ site-packages
                └ requests
                └ <other_dependencies> (i.e. dependencies of the requests package)
                └ ...
```

### **🛠️ Steps to Work with Manylinux wheels**

1. **🔍 Install Python Libraries Using Manylinux wheels**
   Manywheels offers precompiled wheels for many Python libraries that are compatible with different Linux versions used in AWS Lambda. This eliminates the need to compile libraries during deployment, improving the efficiency of the deployment process.

2. **🔎 Search and Download the Library from PyPI**
   - Go to [PyPI](https://pypi.org/project/) and search for the library you want to install.
   - Under the **Download files** section, search for the version compatible with your function runtime. For example, look for `cp311` if you're using Python 3.11.

3. **📋 Copy the Manylinux wheels Link**
   - Right-click the `manylinux` x86_64 version link for the desired version and copy the link address.

4. **📝 Add to Requirements.txt**
   - Paste the copied link into your `requirements.txt` file for the library.

5. **⚙️ Install Dependencies**
   - Use `pip` with the version number to download the modules into the required directory for the Lambda layer:
   ```bash
   pip3.11 install -r requirements.txt --target aws-layer/python/lib/python3.11/site-packages
   ```

### **💡 Why Use Manylinux wheel distribution?**
**Manylinux wheel distribution** is especially useful when you need to install native C extensions or other complex dependencies in an environment like AWS Lambda. By providing precompiled wheels for various Python versions and AWS Lambda-compatible Linux environments, it simplifies the process of setting up Lambda layers.

### **⏰ When to Use Manylinux wheel**
- **⚙️ Complex Dependencies**: If your Lambda function relies on Python libraries that include C extensions or need to be compiled.
- **🌐 Cross-Compatibility**: When you need to deploy to different Python runtime versions (e.g., Python 3.8, 3.9, 3.10) on Lambda.
- **🔄 Reusability**: If you are using the same dependencies across multiple Lambda functions and want to avoid reinstallation.

For more detailed information on Lambda layers, refer to the [AWS Lambda documentation on Python layers](https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html#python-layer-manylinux).
