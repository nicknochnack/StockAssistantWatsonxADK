# Build a stock assistant with watsonx Orchestrate ADK
How to build your own stock assistant using Watsonx Orchestrate. Shown on a bunch of live stages globally in Sydney. 

## See it live and in action 📺
<img src="https://i.imgur.com/L67jivK.gif"/>

# Startup 🚀
1. Create uv project: `uv init`
2. Install python library: `uv add ibm-watsonx-orchestrate`
3. Double check orchestrate version: `orchestrate --version`
4. Get entitlement key from https://myibm.ibm.com/products-services/containerlibrary
5. Rename sample.env file to `.env` and fill out this stuff 
WO_DEVELOPER_EDITION_SOURCE=myibm
WO_ENTITLEMENT_KEY=
WATSONX_APIKEY=
WATSONX_SPACE_ID=
6. Install orchestrate: `uv run orchestrate server start --env-file='.env'`
7. Activate local tenant: `orchestrate env activate local`
8. Start the Chat UI: `uv run orchestrate chat start`
9. Create an agent `uv run orchestrate agents import -f ${SCRIPT_DIR}/agents/ibm_agent.yaml`
10. Import a tool `uv run orchestrate tools import -k python -f "stockprice.py" -r "stocks.txt"`

</br>
# Other References 🔗 </br>
- ToDo...maybe later

# Who, When, Why?

👨🏾‍💻 Author: Nick Renotte <br />
📅 Version: 1.x<br />
📜 License: This project is licensed under the MIT License </br>




