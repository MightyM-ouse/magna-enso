# MAG-US-001 — Animated Magna Living Identity Branding

Status: FINAL  
Epic: MAG-EPIC-003 — Magna Presence and Identity  
Capability Area: Identity / Branding / Command Center Presence  
Product Owner: Vinay / Product Owner  
Priority: P1  

## User Story

As a Magna user, I want Magna to identify appropriate brand-safe locations and display the animated Magna Enso identity across the product, so that Magna has a living, recognizable brand presence without disrupting the existing Command Center layout.

## User Value

This gives Magna a consistent living identity while respecting the current UI structure. Since the product does not yet have a dedicated logo placeholder, Magna should first use the splash/loading screen as the initial placement and then adapt the logo placement per screen where branding is appropriate.

The animated Magna Enso mark should communicate identity, continuity, intelligence, and HELIX energy. It should make Magna feel alive and active, especially when Magna is thinking, without distracting the user or interrupting normal work.

## Product Decisions Confirmed

- The approved animated source asset is `brand-assets/magna_enso_anticlockwise_rotation_slow.gif`.
- The first placement should be the splash/loading screen.
- Logo placement should adapt by screen instead of using the exact same placement everywhere.
- The animated Magna Enso mark is product branding, not only a decorative asset.
- There is currently no dedicated logo placeholder in the UI.
- Magna must identify product-safe branding locations before placing the logo across screens.
- The logo placement must not break or redesign the frozen Magna shell.
- The animation should run continuously.
- The animation should also be used when Magna is thinking.
- The thinking-state animation should use a slightly emphasized variant of the approved animation.
- The animation should not pause when the user is typing or working.
- The outer Enso / Magna ring rotates anticlockwise.
- The center galaxy rotates slower than the outer Enso ring.
- HELIX should show visible energy flowing through it.
- The approved slower rotation speed should be used.
- Reduced-motion accessibility behavior should automatically switch to a static fallback when required.
- The static fallback should be a frame from the approved animation.
- The product should use the best recommended rendering format for performance, accessibility, and visual quality.

## User Flow

1. User opens Magna.
2. Magna displays the animated Magna Enso identity on the splash/loading screen.
3. The outer Magna / Enso form rotates slowly in an anticlockwise direction.
4. The central galaxy rotates more slowly than the outer ring.
5. HELIX shows a visible energy-flow effect through its strands.
6. After the splash/loading screen, Magna identifies suitable brand-safe locations per screen where the logo can appear without disrupting the UI.
7. Magna adapts the logo placement by screen rather than forcing one fixed placement everywhere.
8. When Magna is thinking, Magna uses a slightly emphasized variant of the animated identity.
9. The animation continues while the user navigates, types, or works.
10. If reduced-motion behavior is required, Magna automatically switches to a static fallback frame from the approved animation.
11. The animation does not block interaction, reduce readability, or change the frozen Magna shell structure.

## Acceptance Criteria

- [ ] Magna uses `brand-assets/magna_enso_anticlockwise_rotation_slow.gif` as the approved animated branding source.
- [ ] Magna displays the animated Magna Enso identity on the splash/loading screen as the first placement.
- [ ] Magna identifies appropriate brand-safe locations before placing the logo on additional screens.
- [ ] Logo placement adapts by screen instead of using one fixed placement everywhere.
- [ ] The selected logo locations do not require redesigning the frozen Magna shell.
- [ ] The selected logo locations do not conflict with navigation, command input, system status, tabs, or primary content.
- [ ] The animation runs continuously.
- [ ] The animation is also available for Magna thinking/presence states.
- [ ] Magna uses a slightly emphasized animation variant when Magna is thinking.
- [ ] The animation does not pause when the user types, navigates, or works.
- [ ] The outer Enso / Magna ring rotates anticlockwise.
- [ ] The center galaxy rotates slower than the outer Enso / Magna ring.
- [ ] HELIX strands show a visible energy-flow effect.
- [ ] The HELIX energy flow feels alive and continuous, not flashing or distracting.
- [ ] The animation speed matches the approved slower version.
- [ ] The animation loops smoothly.
- [ ] The animation preserves the original Magna visual identity, colors, layout, and symbolic meaning.
- [ ] The animation does not interfere with command entry, navigation, readability, or user interaction.
- [ ] The animation can be used without changing the frozen Magna shell layout or tab structure.
- [ ] Reduced-motion accessibility behavior automatically switches to a static fallback when required.
- [ ] The static fallback is generated from a frame of the approved animation.
- [ ] The animation does not create excessive performance load.
- [ ] The product uses the most suitable optimized rendering approach for branding usage.

## Out of Scope

- Redesigning the Magna logo.
- Changing the Magna / HELIX symbolic meaning.
- Changing the Command Center shell layout or navigation tabs.
- Adding a large new branding panel unless explicitly approved.
- Adding sound effects.
- Adding user-customizable animation controls.
- Replacing the full roadmap graphic.
- Creating complex 3D galaxy-cluster animation.
- Treating the animation as proof of autonomous activity.
- Using the animation to imply that Magna is executing actions unless a separate thinking/status story defines that behavior.

## Dependencies

- Product dependency: Approved animated Magna Enso branding asset at `brand-assets/magna_enso_anticlockwise_rotation_slow.gif`.
- Product dependency: Static fallback frame generated from the approved animation.
- Design dependency: DES-### — Define splash/loading screen placement and adaptive per-screen branding rules.
- Design dependency: DES-### — Define thinking-state emphasized animation behavior.
- Architecture dependency: ARCH-### — Define preferred animation asset strategy for performance, fallback, accessibility, and maintainability.
- Frontend dependency: FE-### — Implement animated Magna identity rendering on splash/loading screen and approved adaptive screen locations.
- Performance/accessibility dependency: VAL-### — Confirm animation performance, static fallback, and reduced-motion behavior.

## Open Questions

None. Product decisions are confirmed.

## Suggested Downstream Work

These are placeholders only. They are not the product story itself.

### Design Task

DES-### — Review the current Magna shell and define adaptive brand-safe logo placement rules by screen.

### Design Task

DES-### — Define splash/loading screen usage, thinking-state emphasized variant, sizing rules, fallback frame, and animation behavior.

### Architecture Task

ARCH-### — Define preferred animation asset strategy for performance, reduced-motion fallback, and maintainability.

### Frontend Task

FE-### — Implement animated Magna identity rendering on splash/loading screen, thinking-state surfaces, and approved adaptive screen locations.

### Backend Task

BE-### — N/A unless animated brand asset configuration is loaded from local product settings.

### Agent Task

AGT-### — N/A.

### Validation Task

VAL-### — Validate splash placement, adaptive screen placement, animation direction, speed, HELIX energy flow, continuous playback, thinking-state emphasized variant, performance, fallback frame, and reduced-motion behavior.

### Governance Dependency

GOV-### — Confirm the animation is treated as branding/presence only and does not imply autonomous execution unless separately approved.

## Validation Notes

Validation must confirm the product experience, not only asset rendering.

- Does the splash/loading screen placement feel premium and appropriate?
- Are additional placements adapted safely by screen?
- Does the placement preserve the frozen Magna shell?
- Does the animation feel calm, premium, and alive?
- Does it preserve the Magna identity?
- Is the outer ring rotating anticlockwise?
- Is the center galaxy slower than the outer ring?
- Is HELIX energy visibly flowing through the strands?
- Is the approved slower speed used?
- Does the thinking-state variant feel slightly emphasized without becoming distracting?
- Does the animation avoid distracting the user while typing or working?
- Does the UI remain responsive?
- Is the fallback frame taken from the approved animation?
- Does reduced-motion behavior switch correctly to the static fallback?
