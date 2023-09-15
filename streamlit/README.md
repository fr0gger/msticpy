# MSTICPy CoPilot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aka.ms/msticpy-copilot)


MSTICpy is a multifaceted tool designed to be the Swiss Army knife of threat intelligence in the Python ecosystem. Proudly standing as a flagship open-source project under Microsoft's banner, MSTICpy serves as a bridge, connecting our company with a broader external audience, fostering collaboration, and promoting open-source security solutions.

MSTICpy is designed to facilitate investigations from start to finish. This hackathon project aims to introduce a new feature: the integration of LLM with MSTICpy. This integration is set to automate the investigation process, enabling users to efficiently probe threats based on data-driven insights.

Beyond its core functionalities, MSTICpy's vision is to empower users. This new feature will offer the tools for anyone to craft their own DIY Security Copilot, making advanced threat intelligence accessible and customizable.


## Docker instruction
if you wish to host this locally/in-house, you can use below instructions to build docker images and host it. For more detailed instructions, check out Streamlit docs. [Deploy Streamlit using Docker](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)

Build image

`docker build -t msticpy-copilot .`

Run the docker container

`docker run -p 8501:8501 msticpy-copilot`

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.