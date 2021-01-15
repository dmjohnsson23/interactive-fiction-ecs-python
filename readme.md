# Entity Component System for Interactive Fiction

I might be one of the few millennials to have ever played Zork. I don't recall that I ever finished the game, but it got me interested in the concept of interactive fiction, leading me to find and play several shorter interactive fiction titles.

I have set out several times over the course of my programming adventure to create a simple library for interactive fiction games. Every time the project grew too big, messy, and complicated. Every time I abandoned the project and decided to move on to other things.

I recently decided to try again, this time using the [ECS (entity component system)](https://en.wikipedia.org/wiki/Entity_component_system) architecture. I thought it might be overengineering to do so, as the pattern is more common in more complex video game engines. However, I wanted to get familiar with the ECS pattern so I went ahead with it anyway.

I have actually been pleasantly surprised by just how well this pattern seems to be working, even for something much simpler than a video game. With just a handful of components, I have been able to define a great deal about game entities. From rooms, to player inventory and movement, to items lying around, and interactions between items, I have been able to define all this with a grant total of 7 different (very simple) component types.

This is a work in progress, not usable at all right now. Huge holes missing in the functionality. But this project seems to be coming together really well, and I am excited to see where it goes.