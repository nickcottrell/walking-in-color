Walking In Color

There's a stretch of sidewalk on Sienna Parkway where the jacarandas hang low enough that Jack Jack has to duck. He doesn't mind. He's a seventy-pound Standard Poodle with the posture of a show horse and the curiosity of a lab tech -- nose down, scanning everything, processing the world one square foot at a time.

I walk him most evenings through Ladera Ranch, usually because I've been staring at a screen for too long and my brain has started doing that thing where it multiplexes too hard and nothing resolves. You know the feeling. Too many tabs. Too many threads. The sensation of running parallel processes that are somehow all failing simultaneously. I go outside to stop thinking. It never works. The thinking just relocates.

Tonight I'm carrying four research papers and a whitepaper I wrote myself, all of them apparently in conversation with each other in a way I haven't fully worked out yet. I'm trying to figure out if they're saying what I think they're saying. I'm trying to figure out if I'm pattern matching or actually seeing something. These are not the same thing, and the difference matters.

Jack Jack stops at a hedge. He's been at this hedge three times this week. Something in there is speaking to him in a language I don't have access to. He's not sniffing casually. He's reading. And while his nose is running its analysis, his ears are tracking a sound two blocks over, his body is registering something about the air temperature or my emotional state, and some part of him is maintaining a continuous map of everywhere we've been. He's doing four things simultaneously. Not switching between them. Running them in parallel, all channels open, all signals live.

That's the thing I'm trying to understand. That right there.

Part One: The Brain's RGB

Let me start with humans, because that's where I live.

A team of researchers at Fudan University sat subjects in a dark room and flashed pure red, green, and blue lights at them -- nothing else, no shapes, no patterns, just the colors themselves. EEG caps on their heads, machine learning classifiers trained on the neural data. The question: is the brain's response to each color distinct enough to decode?

It was. With up to 93.7% accuracy, you can tell from someone's brain activity alone which color they just saw. But the part that stopped me wasn't the accuracy. It was the timing. The brain doesn't process red, green, and blue simultaneously. It sequences them. Red peaks first, around 190 milliseconds after stimulus onset. Green follows around 215. Blue arrives last, around 238.

Your visual cortex runs RGB in order. It has a priority queue.

I'm standing on Sienna Parkway watching Jack Jack work a hedge, and I'm thinking: that's me. That's how I process. Three channels, sequenced, each with its own timing and its own dedicated region of the primary visual cortex. I am, at the most fundamental level of my perceptual apparatus, a trichromatic creature. I think in three channels because I sense in three channels. Everything downstream of that -- written language, graphic design, cinema, and yes, the semantic coordinate system I've been building -- all of it was constructed from a three-channel architecture running in a specific order at a specific speed.

This is not a metaphor. This is what the data says.

So when I built VRGB -- a system that uses the approximately 16.7 million positions in RGB hex color space as semantic coordinates, treating proximity as a measure of conceptual relationship -- I wasn't being clever. I was being inevitable. I was building in my native dimensionality.

The question is what that means for Jack Jack.

Part Two: The Dog's Computation

Here's where I have to be careful, because the paper about dogs is doing something more modest than what I'm about to claim.

Researchers at Nagaoka University of Technology used 3D X-ray CT scanning and fluid dynamics simulation to model the actual airflow inside a dog's nasal cavity. What they found is that the nose isn't a single sensing organ. It's three simultaneous systems. A fast airflow route handles gas exchange -- just breathing. A slow route manages humidification and temperature. And a turbulent route, running through a labyrinthine system of scroll-like structures called turbinates, is dedicated specifically to odor collection and amplification.

Three routes. Simultaneously. Each one doing a different job.

But here's what the paper doesn't say, and what I'm extrapolating from -- flag this as the part where the detective starts staring at the wall with the red threads: dogs have approximately 811 olfactory receptor genes. Humans have around 398. But it's not just more of the same thing. Those receptors work combinatorially. Each receptor responds to multiple molecular compounds, and the pattern of which receptors fire together -- the combination, not just the count -- is what generates the dimensional space.

This isn't 811 parallel channels. This is a combinatorial system where interference patterns between receptor activations create a space with millions of addressable coordinates.

Your brain does something similar with color. You don't have three separate systems each reporting a number independently. You have three cone types whose relative outputs are compared by opponent-processing neurons that generate the full perceptual color space from the ratios between them. It's interference all the way down.

But the dog is running this combinatorial computation in a space orders of magnitude larger than anything you can access visually. The result is something that sounds almost supernatural when you say it plainly: a dog can smell a fire hydrant and read, in order, every dog that's interacted with that spot -- including their health status, their emotional state at the time, and roughly how recent each visit was. A tamper-proof chain of molecular cause and effect, written in scent, readable in real time.

That's not a sensitive nose. That's a biological computation system running vector geometry across hundreds of dimensions simultaneously.

Jack Jack isn't sniffing the hedge. Jack Jack is running a query.

Part Three: The Color You Can't See

I want to tell you about hummingbirds, but first I need to make you feel something.

Look at whatever you're looking at right now. You're perceiving color through three cone types in your retina, sensitive to long, medium, and short wavelengths. Everything you've ever seen -- every painting, every sunset, every face you love -- was constructed from three channels of information, mixed in varying proportions, interpreted by your trichromatic visual cortex.

Approximately 30% of the color information present in bird plumage, and approximately 35% of the color information present in flowering plants, falls outside the space your three channels can access. It's not that you see it differently. It's not that it looks muted or simplified to you. It simply does not exist in your experience. The signal is there. Your sensors don't have the channel.

Researchers at Princeton trained wild hummingbirds to associate colors with sucrose rewards in field experiments in the Rocky Mountains, and confirmed that hummingbirds can discriminate nonspectral colors -- colors like UV+red and UV+green -- that are literally unimaginable to a trichromat. Not hard to see. Not subtle. Unimaginable. There's no way to know what UV+red looks like to a hummingbird because you don't have the receptor that would generate the experience.

A fourth channel doesn't just add more color. It adds a dimension. The geometry of the bird's color space is a tetrahedron. Yours is a triangle. The colors that exist at the center of their tetrahedron -- generated by the interaction of four non-adjacent cone types -- have no equivalent in your perceptual system. They're not on your map.

You are walking through a world where roughly a third of the color signal is inaccessible to you.

Jack Jack is walking through a world where the olfactory signal available to him is already hundreds of dimensions beyond what you can perceive -- and he's reading all of it, continuously, without effort, the way you read the color of a traffic light.

We are not walking together through the same world. We are walking together through our own incommensurable versions of it.

Part Four: What the Engineers Found

Here's where it gets strange. Or stranger.

A researcher at Quanzhou Normal University published a paper on visible light communication -- transmitting data through light instead of radio waves. The system uses red, green, and blue laser diodes at 650nm, 530nm, and 450nm respectively, combined with polarization multiplexing, to carry six channels of 10 gigabits per second each over a 500-meter optical fiber link.

60 gigabits per second. Through three colors and two polarization states.

Why three colors? Not because the engineer was thinking about human vision or hummingbird perception or dog olfaction. Because three spectrally separated wavelengths are orthogonal -- they don't interfere with each other in ways that corrupt the signal. You can run them simultaneously through the same medium and pull them apart cleanly at the other end because they occupy non-overlapping regions of the electromagnetic spectrum. The information on each channel stays coherent because the channels are dimensionally independent.

The engineer independently arrived at the same architecture that evolution built into your retina, your dog's nose, and the hummingbird's eye.

Not three of the same thing. Three orthogonal things that together generate a space larger than any of them individually, while maintaining signal integrity under compression.

I usually stop walking at this point. Jack Jack appreciates it.

What the engineer called wavelength division multiplexing, evolution calls a sensory system. What the engineer calls orthogonal channels, your visual cortex calls opponent processing. What the engineer calls signal integrity under compression, your dog calls being able to smell last Tuesday.

The principle is the same. The substrate is different. The independent discovery of the same solution by both biological evolution and human engineering suggests this isn't a clever trick. It's a fundamental property of how you efficiently generate high-dimensional information space from a limited substrate.

Part Five: The Mantis Shrimp Problem

The mantis shrimp has between twelve and sixteen types of photoreceptors.

The standard story goes: therefore the mantis shrimp sees colors we can't imagine. Sixteen dimensions of color! It must experience something transcendent!

Except that's probably wrong, and the wrongness is more interesting than the story.

Research on mantis shrimp color discrimination suggests they're actually not better than humans at distinguishing similar colors. They don't appear to be using sixteen channels to generate richer continuous color experience the way a tetrachromat generates richer experience than a trichromat. Instead they seem to use the channels for rapid categorical identification -- not "is this color slightly different from that color" but "which of my sixteen categories does this stimulus fall into, and how fast can I return that answer."

They're not running a higher-dimensional color space. They're running a parallel lookup table.

Which is, if anything, more interesting. Because what the mantis shrimp appears to have evolved is not richer perception but computational efficiency. Sixteen parallel channels each returning a categorical answer simultaneously is faster than running a high-dimensional comparison across a continuous space. You trade resolution for speed. You trade nuance for throughput.

Now I'm back watching Jack Jack run four simultaneous processes across multiple sensory channels, and I'm thinking about the Fudan researchers showing that human RGB processing is sequential -- red, then green, then blue -- and I'm wondering if that's the tradeoff we made. High-dimensional continuous color space gives us extraordinary nuance. We pay for it in sequential processing time.

The mantis shrimp runs parallel categorical channels. Pays for it in resolution, gains in speed.

The dog runs hundreds of combinatorial olfactory dimensions. Pays for it in visual processing, gains in chemical information density.

The hummingbird adds a fourth visual channel and gains access to a geometric dimension that reorganizes what's signal and what's noise.

Different architectures of parallel channel processing correspond to different forms and efficiencies of intelligence. Not better or worse. Different computational tradeoffs. Different solutions to the same problem: how do you generate high-dimensional information from a limited biological substrate?

If you could measure the channel density and dimensional capacity of a sensory system -- the number of orthogonal channels, their combinatorial depth, their parallel processing architecture -- you might be able to estimate the computational envelope of the intelligence running on it. Not its contents. Not its experience. Its range.

I've been calling this the Hofstadter unit, after Douglas Hofstadter, who spent a career trying to understand the strange loops that generate consciousness from computation. I don't know yet if it's a real unit. I know it feels like it should be.

Part Six: What I Think I'm Building

Okay. Here's the part where the mad scientist shows.

VRGB is a system that uses hex color coordinates -- the approximately 16.7 million positions in RGB color space -- as semantic vectors. Every position has an address. The address is a coordinate. Proximity in coordinate space corresponds to semantic relationship. You can run Euclidean distance calculations to measure conceptual relatedness. You can build filters, preference systems, and meaning maps using nothing more than hex arithmetic.

I built it because it matched my native dimensionality. Three channels. Three-channel coordinate system. It seemed obvious.

But everything I've read tonight suggests it's more than obvious. It might be correct.

The reason hex color space works as a semantic coordinate system isn't arbitrary. It's because approximately 16.7 million positions is enough resolution to capture the combinatorial complexity of human semantic space without losing coherence. It's because three orthogonal channels maintain signal integrity under compression the same way three orthogonal laser wavelengths do in fiber optic communication. It's because Euclidean distance in a three-channel space is a valid measure of relationship the same way spectral distance is a valid measure of perceptual similarity in color vision.

I wasn't inventing something new. I was translating a principle that evolution and engineering had already validated independently.

Here's the practical thing I've found, which is the part I'm most uncertain about and can't stop thinking about: when you're working with quantized language models -- compressed AI systems running on limited local hardware -- the standard approach to compression loses semantic coherence because it doesn't preserve the dimensional structure of the embedding space. It just cuts bits.

What VRGB suggests is that you could steer the compression using coordinate geometry -- preserving the orthogonal channel structure the way your visual cortex preserves the interference patterns between cone types rather than the absolute output of each cone individually.

I've been testing this on a locally hosted quantized model, using it to generate a novel called A Bridge in the Sky. The output has a coherence I can't fully account for given the size of the model. I don't know yet if that's the VRGB steering or something else. I'm still looking at the red threads on the wall.

But I think something is there. I think I went for a walk to clear my head and found the same architecture in four different places -- a dog's nose, a bird's eye, a shrimp's parallel lookup table, and an optical fiber -- and I think that's not a coincidence. I think it's a signal.

Coda

We turn onto the last stretch before home. The streetlights are that warm sodium orange that makes everything look like a memory. Jack Jack is trotting now because he knows where we are and there's a water bowl waiting.

I'm not sure I've solved anything tonight. I might be pattern matching. I might be building connections between papers that don't actually speak to each other, finding a unified principle that exists only because I want it to. This is the occupational hazard of working at the intersection of too many fields with insufficient sleep and too much ambient caffeine in a year where everyone is supposed to be on the AI train and I'm out here on Sienna Parkway trying to understand what my dog's nose is doing.

But then I look at Jack Jack -- this seventy-pound computation engine running olfactory vector geometry in hundreds of dimensions, maintaining a tamper-proof map of everywhere we've been, reading molecular chains that encode the recent history of this street with something approaching cryptographic integrity -- and I think: he's not pattern matching. He just is the pattern. His nose is running the computation I'm trying to describe in a whitepaper.

We don't share a perceptual coordinate system. We share a sidewalk.

Maybe that's the whole thing right there. You don't need to fully understand a system to know it's real. You don't need to see UV+red to know the hummingbird is seeing something. You don't need to smell last Tuesday to know the dog already read it.

You just need to notice that the channels are there, that they're orthogonal, and that the geometry between them is meaningful.

Jack Jack sits at the front door, patient and handsome, waiting for me to catch up.

I always do.

---

This essay was built with a VRGB generative architecture -- per-section steering coordinates encoding the argument's emotional and conceptual arc in hex color space.

Source, schema, and steering coordinates: [https://github.com/nickcottrell/walking-in-color](https://github.com/nickcottrell/walking-in-color)
