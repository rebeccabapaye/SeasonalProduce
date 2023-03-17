# Overview

Supermarkets don't always have the produce shoppers expect to be available, and shoppers may not know which fruits and vegetables are in season. Plus, manually looking up that information on a phone while navigating aisles with a basket full of groceries is inconvenient - it's easier to ask an intelligent assitant. 

The Seasonal Produce capsule for Bixby will allow users to request information about a specific item or season to help determine what produce to purchase. The information will be stored and managed in a SQLite database hosted SOMEWHERE.

## Product Manager
* Rebecca Bapaye

## Developers
* Rebecca Bapaye (Database, Capsule)
* Ameya Bapaye (Capsule)

# Objective

The objective of this project is to increase the ease with which people can look up seasonal produce information on the go.

# Context
Customer personas, use cases, competitive landscape, and other supporting material that will help the team develop a deeper understanding.
What does the team need to know to do their job successfully?
What informed this release? Was it a market trend? Do you have customer interviews to share?
Who are your target personas? What use cases have you identified?
Is there high-level information about future roadmap plans worth sharing?

## Competitive Landscape

Bixby is one of four major intelligent assistants in the current market. Its main competitors are Google's Assistant, Amazon's Alexa, and Apple's Siri. The main benefits and drawbacks of each are as follows.

## Bixby
### Benefits
* Guaranteed Reach: Natively available on most Samsung devices (mobile, watch, fridge, tv, etc.)
* Greater Ability for Visual Presentation: Bixby provides greater functionality for creating comprehensive views for displaying data
* Dedicated IDE for Bixby Development: [Bixby Studio](https://bixbydevelopers.com/) is built specifically for Bixby development allowing devs to focus on functionality while Bixby Studio handles boilerplate code and the latest Capsule approval requirements
### Drawbacks
* Dedicated IDE needs Familiarization: Having to use Bixby Studio requires upfront developer investment to learn the IDE
* No Direct Monetization: Bixby does currently allow for in-capsule monetization

## Google Assistant
### Benefits
* Guaranteed Reach: Natively available on all Android devices
### Drawbacks
* Greater Up-Front Development and Continued Maintenance: Google plans to sunset conversational Actions in [June 2023](https://developers.google.com/assistant/ca-sunset) in favor of App Actions. App Actions simply provide a hook for Google Assistant to access functionality available in an existing Android app. This would require the development and maintenance of a Seasonal Produce app in addition to the Action
* Greater Friction for User Enrollment: Users will have to download an Android app and enable a Google Action to search for seasonal produce using Google Assistant

## Amazon Alexa
### Benefits
* Guaranteed Audience: Amazon enjoys the majority marketshare in the online store, e-book, and audiobook marketplace.
* Well-Developed Skill templates: Amazon provides [templates](https://developer.amazon.com/en-US/alexa/alexa-skills-kit) to allow developers to quickly build and deploy Skills
### Drawbacks
* Limited Devices: Amazon's hardware does not have relevant marketshare
## Apple Siri
### Benefits
* Guaranteed Reach: The Apple ecosystem solely supports Siri which creates a dedicated userbase that can only use one platform
### Drawbacks
* Greater Up-Front Development and Continued Maintenance: Apple requires an app for Siri to hook into using the [SiriKit](https://developer.apple.com/siri/). This would require the development and maintenance of a Seasonal Produce app


# Assumptions

* Bixby is the correct intelligent assistant to use for this project because Google Assistant has recently curtailed third party development for Google Actions and Amazon does not have enough marketshare in mobile devices to warrant programming an Alexa Skill
* Depending on the initial reception and long term success of this project, there will be additional upkeep and costs associated with hosting the database and polling it for information

# Scope

The scope of this project is to provide Bixby users (in the United States) a means of checking if a fruit or vegetable is in season, or requesting a list of fruits and vegetables that are in season.

* The current priority will be fruits and vegetables commonly found in supermarkets in the United States, but eventually more varied items may be added to the database
* In the future, functionality may be added to allow users to request the addition of specific items not currently listed in the database

# Requirements

## User Stories

User 1 wants to know whether a specific fruit or vegetable is in season.
User 1: Are apples in season right now?
Capsule provides answer.

User 2 wants to know what produce in general is in season right now.
User 2: What is in season?
Capsule provides a list of fruits and vegetables that are in season.

User 3 is at the supermarket but doesn't know what kind of produce they want to buy.
User 3: Which vegetables are in season right now?
Capsule provides a list of in-season vegetables.

User 4 is making their shopping list at home and wants to know what fruits and vegetables are best purchased in winter.
User 4: What produce is in season in the winter?
Capsule provides a list of in-season fruits and vegetables for winter.

User 5 is at the grocery store, in the produce section, and is trying to select both fruits and vegetables, but they don't know what is in season.
User 5: What fruits are in season right now?
Capsule provides a list depending on the user's season.
User 5 continues the conversation: What about vegetables?
Capsule provides a list from the same season.

# Design

Screenshots of the look

# Performance

Metric for success to be decided. Some metrics that will be considered are accuracy of results, the capsule rating and/or customer satisfaction, and number of user reports.

# Open questions

* Will the team eventually branch out to other intelligent assistants?
* Are there regional fruits and vegetables either in or outside the US that will be missing from the initial scope of the capsule?
* Will the capsule be expanded to other regions or localities?
* What is the capsule's source of truth for produce included in the database?