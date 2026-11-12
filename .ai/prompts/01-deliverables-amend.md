We're taking a break from the next task to explore and evaluate an idea. I'm starting a new branch for this exploration.

I think some of the deliverables should be tailored for usage:
- Powerpoint presentations and study textbook PDF for learners
- Powerpoint presentations and presentation notes / speech PDF for presenters

I'm undecided if the lessons markdown should follow suit.

The goal is to have the deliverables serve a specific role (learning vs teaching):
- Learners do not need to know presentation notes, timeframe, preparation checklist, etc ...
- Presenter want an efficient document with preparation checklists, timeframes, presentation notes and instructions, etc ...

Evaluate thoroughly. Propose how to implement, suggestions, or improvements.


-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

Replies to your questions:
1. Participants are given the books AFTER the sessions, but explore making this choice a build config for AFTER vs BEFORE.
2. Yes, a PDF instead of a PPTX makes sense. Approved.
3. Yes, no split. A lesson should be a self-contained unit that can then be used to make the deliverables.
4. As recommended.
5. As recommended.

Additions / clarifications on your suggestions:
1. For the learner:
	- The goal is to provide a pleasant study textbook that follows best practices and industry standards in terms of education and pedagogy, and provides a relaxed and easy-to-read experience.
2. For the teacher / presenter:
	- The goal is efficiency.
	- Time tables should be either fixed time (from a start time provided from config), or relative. A configuration option from a `.env` file should toggle between the two (also add a committed `.env.example` for reference).
	- Adjust type, style, and formatting (maybe even some icons / illustrations) so that it's easier to use (for a document's given usage) in a presentation context (i.e., in a room, standing, probably a bit far from a screen, projecting, etc.).
	- The guide shouldn't repeat the learner's text indeed.
3. Design:
	- Default to US formats (letter, etc.), but provide a config to switch to ISO formats (A4, etc.).
4. Your three fix suggestions are all agreed and approved as suggested.
5. Your "data about a specific delivery" risk point is correct. Go with your suggestion of passing them in from a non-committed file. Provide a committed example file for reference.
6. Your "Releases" risk point is also correct. In addition to what you suggest, releases will bundle the learner's documents and the presented documents into two zip files, properly named. Since this is a public project reusable by other people, no actual built deliverables will be attached to releases on GitHub (only the source code, i.e., lesson markdown, build scripts, etc.). Propose gitignores to implement this.

While we're at it:

7. This is a good occasion to revise our design.
	- The revision should follow the rules and skills already set.
	- The current design is the same for both the learner and teacher. That's not necessarily an issue.
	- The current design is too bland and boring. Explore modern, more interesting designs that invoke a bit more energy while maintaining a professional look.
	- All PPTX and PDFs seem to have a lot of text. It would be nice to add visualization / artwork / illustrations where applicable, every now and then.
	Build samples using a few of the existing core tracks lessons, then ask me for my decision on which to keep.
8. Re-evaluate the presenter's timing tables along the new decisions made so far. It seems to me some parts might be too tight. We should always err on the more relaxed side, allow for ample room interactions, practical examples / exercises, etc. The 90 to 120 minutes constraint is more of an ideal than a strict requirement; just remember to go back and schedule 15-minute pause points every 90 minutes or so (at what would be good stopping points) if it goes beyond 3 hours.

Re-evaluate all of this thoroughly and provide an action plan adapted to your capacities. Do not act until I specifically provide permission to implement.

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

1.2. in response to "What the setting can't fix", your suggestion is acceptable. In that mode, a warning should be automatically generated.

3. in response to "What I can and can't do":
	- > I can't produce figurative illustrations or photos, so the samples stay geometric.

		is not acceptable. Suggest tools or solutions. This machine is pretty strong: Ryzen 7950X, GeForce RTX 4090, 64GB DDR5 5600Mt/s.

Decisions:
1. No worktree. There is no other active session using `deliverables-by-role`, I specifically made this branch for this exploration and change. You are allowed to work on this branch directly.
2. Keep 2 hrs as the main format, with an option for 2x 90 minutes
3. Approved as recommended.
4. Approved as recommended.
5. Approved as recommended.
6. Approved as recommended. Render actuall PPTX / PDFs. Include any new weights, as needed.
7. Implement up to phase 1. All locked files involved in that phase are approved for edits, for this phase.

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

Illustration, option 1 only, with comfyui.

  Replies:
  1. Then just make the 2x90 minutes the default. Do not cut reuquired topics. Drop 2hr version
  2. Accepted
  3. Yes
  4. Yes

  Committed and pushed.