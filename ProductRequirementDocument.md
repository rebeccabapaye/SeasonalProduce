# Overview

Supermarkets don't always have the produce shoppers expect to be available, and shoppers may not know which fruits and vegetables are in season. Plus, manually looking up that information on a phone while navigating aisles with a basket full of groceries is inconvenient - it's easier to ask an intelligent assistant. 

The Seasonal Produce capsule for Bixby allows users based in the United States to request information about a specific item or season to help determine what produce to purchase. The capsule utilizes information from the [U.S. Department of Agriculture SNAP-Ed Seasonal Produce Guide](https://snaped.fns.usda.gov/seasonal-produce-guide). The information is stored within the capsule as a JSON object.

## Product Manager
* Rebecca Bapaye

## Developers
* Rebecca Bapaye (Database, Capsule)
* Ameya Bapaye (Capsule)

# Objective

The objective of this project is to increase the ease with which people can look up seasonal produce information on the go.

# Context

## Competitive Landscape

Bixby is one of four major intelligent assistants in the current market. Its main competitors are Google's Assistant, Amazon's Alexa, and Apple's Siri. The main benefits and drawbacks of each are as follows.

## Bixby
### Benefits
* Guaranteed reach: Natively available on most Samsung devices (mobile, watch, fridge, TV, etc.)
* Greater ability for visual presentation: Bixby provides greater functionality for creating comprehensive views for displaying data
* Dedicated IDE for Bixby development: [Bixby Studio](https://bixbydevelopers.com/) is built specifically for Bixby development allowing devs to focus on functionality while Bixby Studio handles boilerplate code and the latest Capsule approval requirements
### Drawbacks
* Dedicated IDE needs familiarization: Using Bixby Studio requires upfront developer investment to learn the IDE
* No direct monetization: Bixby does not currently provide in-capsule monetization

## Google Assistant
### Benefits
* Guaranteed reach: Natively available on all Android devices
### Drawbacks
* Greater up-front development and continued maintenance: Google plans to sunset conversational Actions in [June 2023](https://developers.google.com/assistant/ca-sunset) in favor of App Actions. App Actions simply provide a hook for Google Assistant to access functionality available in an existing Android app. This would require the development and maintenance of a Seasonal Produce app in addition to the Action
* Greater friction for user enrollment: Users will have to download an Android app and enable a Google Action to search for seasonal produce using Google Assistant

## Amazon Alexa
### Benefits
* Guaranteed audience: Amazon has the majority marketshare in the online store, e-book, and audiobook marketplace.
* Well-developed Skill templates: Amazon provides [templates](https://developer.amazon.com/en-US/alexa/alexa-skills-kit) to allow developers to quickly build and deploy Skills
### Drawbacks
* Limited devices: Amazon's hardware does not have relevant market share
## Apple Siri
### Benefits
* Guaranteed reach: The Apple ecosystem solely supports Siri which creates a dedicated userbase that can only use one platform
### Drawbacks
* Greater up-front development and continued maintenance: Apple requires an app for Siri to hook into using the [SiriKit](https://developer.apple.com/siri/). This would require the development and maintenance of a Seasonal Produce app


# Assumptions

* Bixby is the correct intelligent assistant to use for this project because Google Assistant has recently curtailed third party development for Google Actions and Amazon does not have enough marketshare in mobile devices to warrant programming an Alexa Skill
* Depending on the initial reception and long-term success of this project, there will be additional upkeep and costs associated with hosting the database and polling it for information

# Scope

The scope of this project is to provide Bixby users a way to check whether a fruit or vegetable is in season. The user can also request a list of all fruits and vegetables that are currently in season.

* The current priority will be fruits and vegetables commonly found in supermarkets in the United States, but eventually more varied items may be added to the database
* In the future, functionality may be added to allow users to request the addition of specific items not currently listed in the database

# Requirements

## User Stories

*User 1 wants to know whether a specific fruit or vegetable is in season.*<br>
User 1: Are apples in season right now?<br>
Capsule: Provides answer.

*User 2 wants to know all the produce that is in season right now.*<br>
User 2: What is in season?<br>
Capsule: Provides a list of fruits and vegetables that are in season.

*User 3 is at the supermarket but doesn't know what kind of produce they want to buy.*<br>
User 3: Which vegetables are in season right now?<br>
Capsule: Provides a list of in-season vegetables.

*User 4 is making their shopping list at home and wants to know which fruits and vegetables are best purchased in winter.*<br>
User 4: What produce is in season in the winter?<br>
Capsule: Provides a list of fruits and vegetables that are in season in the winter.

*User 5 is at the grocery store trying to select both fruits and vegetables, but they don't know what is in season.*<br>
User 5: What fruits are in season right now?<br>
Capsule: Provides a list depending on the user's season.<br>
User 5 (continuing the conversation): What about vegetables?<br>
Capsule: Provides a list from the same season.

# Performance

Metrics for success to be decided. Some metrics that will be considered are accuracy of results, the capsule rating and customer satisfaction, and number of user reports.

# Open questions

* Will the team eventually consider other intelligent assistants?
* Are there regional fruits and vegetables either in or outside the US that will be missing from the initial scope of the capsule?
* Will the capsule be expanded to other regions or localities?
* Will the capsule have more than one source of truth for produce included in the database?
