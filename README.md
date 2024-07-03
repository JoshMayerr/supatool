![banner]

![GitHub License](https://img.shields.io/github/license/mashape/apistatus)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/joshmayerr/agent-toolbox)

# The Supatool Registry 🪄
An open source registry of (super) *useful* tools to be used by autonomous agents.

What is the Supatool Registry?
--------------------------

All startups building agents like MultiOn, Induced, and even Rabbit all have a core reliance on automating browsers to take actions on their users' behalf. This strategy is fundamentally slow. It's not exactly easy to see today, but as better models come with faster inference time, the time it takes to run playwright and click buttons on a screen remains the same. Clicking buttons adds a global minimum for how quick a browser-based agent can run. Not only speed, but any auth based actions have [inherit security concerns](https://josephthacker.com/ai/2024/04/26/rabbit-r1-innovative-device-security-concerns.html) and Rabbit has already been [under fire](https://twitter.com/aaronwhite/status/1785867544106049950) for it.

The main reason startups choose the browser based path is because it could be more widely applicable. The only reason this is true is because of the lack of public APIs that exist today. Before agents, there was no real need for products to publish them. But now, there is potential for an entirely new interface for people and agents to interact with products. The main blocker to this idea is access to public APIs!

That is why the Supatool Registry is trying to build a large catalog of first-party public APIs which can be used as tools by agents. The more people using API-based agents, the better incentive for companies to simply release their OpenAPI specifications and allow agents to use their products as efficiently as possible, by agents.

There are three parts to Supatool:
1. The Registry
2. Supatool Search
3. Example agents (or "clients") that use Supatool

What's inside?
--------------------------
* Registry of first-party tools (ex. Google Calendar, Notion, Spotify, etc.)
* OpenAPI specifications for all tools
* Additional metadata to search across tools
* Example agents using langchain
* Langchain and Llamaindex integration (coming soon)
* Update definitions on at least a weekly basis (coming soon)

Add your own Tools!
--------------------------
Documentation coming soon.

Roadmap 🚧
--------------------------
- [ ] Compile 100+ raw OpenAPI specs
- [ ] Transform raw specs into indexed/searchable Supatool format
- [x] Simple search endpoint that returns tools
- [x] Example agent that uses search endpoint

Licenses
--------------------------
All API definitions contributed to project by authors are covered by the [CC01.0](https://creativecommons.org/publicdomain/zero/1.0/) license.<br>
All API definitions acquired from public sources under the [Fair use](http://en.wikipedia.org/wiki/Fair_use) principle.

Many of the API specifications are sourced from [apis.guru](https://apis.guru). Thank you for your contributions to the OSS community.

[banner]: /banner.png "supatool"
