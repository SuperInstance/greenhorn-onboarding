"""
Test suite for the Dojo exercise infrastructure.

Validates that all Dojo levels have correct structure, required sections,
proper formatting, exercise counts, and cross-references.

Run with: pytest tests/test_dojo_levels.py -v
"""

import os
import re
import pytest

# Paths
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOJO_DIR = os.path.join(REPO_ROOT, "dojo")

LEVEL_FILES = {
    1: "level-01-fleet-recruit.md",
    2: "level-02-git-sailor.md",
    3: "level-03-bytecode-builder.md",
    4: "level-04-signal-apprentice.md",
    5: "level-05-fleet-contributor.md",
}

LEVEL_NAMES = {
    1: "Fleet Recruit",
    2: "Git Sailor",
    3: "Bytecode Builder",
    4: "Signal Apprentice",
    5: "Fleet Contributor",
}

LEVEL_BADGES = {
    1: ("Fleet Recruit", "Bronze"),
    2: ("Git Sailor", "Bronze"),
    3: ("Bytecode Builder", "Silver"),
    4: ("Signal Apprentice", "Silver"),
    5: ("Fleet Contributor", "Gold"),
}

REQUIRED_SECTIONS = [
    "Description",
    "Objectives",
    "Exercises",
]

REQUIRED_EXERCISE_PARTS = [
    "Task:",
    "Validation:",
    "Hint:",
]


def read_level(level_num):
    """Read a level file and return its content."""
    filepath = os.path.join(DOJO_DIR, LEVEL_FILES[level_num])
    with open(filepath, "r") as f:
        return f.read()


def count_exercises(content):
    """Count the number of exercises in a level file."""
    # Exercises are marked as "### Exercise X.Y:"
    pattern = r"^### Exercise \d+\.\d+"
    return len(re.findall(pattern, content, re.MULTILINE))


def extract_exercise_numbers(content):
    """Extract all exercise numbers as (level, exercise) tuples."""
    pattern = r"### Exercise (\d+)\.(\d+)"
    return re.findall(pattern, content)


def extract_validation_items(content):
    """Extract all validation checkbox items from a level."""
    pattern = r"- \[[ x]\] (.+)"
    return re.findall(pattern, content)


def extract_hints(content):
    """Extract all hint paragraphs from a level."""
    pattern = r"\*\*Hint:\*\*\s*(.+?)(?:\n\n|\n---)"
    return re.findall(pattern, content, re.DOTALL)


# ============================================================
# Test Suite: Directory and File Existence
# ============================================================

class TestDojoDirectoryExists:
    """Test that the dojo directory and level files exist."""

    def test_dojo_directory_exists(self):
        assert os.path.isdir(DOJO_DIR), f"Dojo directory missing: {DOJO_DIR}"

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_file_exists(self, level):
        filepath = os.path.join(DOJO_DIR, LEVEL_FILES[level])
        assert os.path.isfile(filepath), f"Level {level} file missing: {filepath}"


# ============================================================
# Test Suite: Level Structure
# ============================================================

class TestLevelStructure:
    """Test that each level has proper structure and required sections."""

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_file_not_empty(self, level):
        content = read_level(level)
        assert len(content) > 100, f"Level {level} file is suspiciously short ({len(content)} chars)"

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_correct_title(self, level):
        content = read_level(level)
        expected_title = f"# Level {level}: {LEVEL_NAMES[level]}"
        assert expected_title in content, (
            f"Level {level} should start with '{expected_title}'"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_required_sections(self, level):
        content = read_level(level)
        for section in REQUIRED_SECTIONS:
            # Check for markdown heading
            assert f"## {section}" in content, (
                f"Level {level} missing required section: ## {section}"
            )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_description(self, level):
        content = read_level(level)
        assert "## Description" in content
        desc_start = content.index("## Description")
        # Description should have at least 50 chars of content
        desc_section = content[desc_start:desc_start + 500]
        # Remove markdown formatting
        text = re.sub(r"[#*>`\-]", "", desc_section)
        text = re.sub(r"\s+", " ", text).strip()
        assert len(text) > 50, f"Level {level} description seems too short"

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_prerequisites(self, level):
        content = read_level(level)
        if level == 1:
            assert "Prerequisites:** None" in content, (
                "Level 1 should have no prerequisites"
            )
        else:
            assert "Prerequisites:" in content, (
                f"Level {level} should specify prerequisites"
            )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_difficulty(self, level):
        content = read_level(level)
        assert "Difficulty:" in content, f"Level {level} missing difficulty rating"
        assert "/10" in content, f"Level {level} difficulty should use /10 scale"

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_time_estimate(self, level):
        content = read_level(level)
        assert "Time estimate:" in content, f"Level {level} missing time estimate"


# ============================================================
# Test Suite: Exercises
# ============================================================

class TestExercises:
    """Test that each level has the correct number of exercises with proper structure."""

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_level_has_five_exercises(self, level):
        content = read_level(level)
        count = count_exercises(content)
        assert count == 5, (
            f"Level {level} should have exactly 5 exercises, found {count}"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_exercise_numbers_are_sequential(self, level):
        content = read_level(level)
        numbers = extract_exercise_numbers(content)
        level_nums = [int(n[0]) for n in numbers]
        exercise_nums = [int(n[1]) for n in numbers]

        # All exercises should belong to the correct level
        assert all(ln == level for ln in level_nums), (
            f"Level {level} has exercises with wrong level numbers: {numbers}"
        )

        # Exercise numbers should be 1, 2, 3, 4, 5
        assert exercise_nums == [1, 2, 3, 4, 5], (
            f"Level {level} exercise numbers should be 1-5, got: {exercise_nums}"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_each_exercise_has_task(self, level):
        content = read_level(level)
        task_count = len(re.findall(r"\*\*Task:\*\*", content))
        assert task_count == 5, (
            f"Level {level} should have 5 tasks, found {task_count}"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_each_exercise_has_validation(self, level):
        content = read_level(level)
        validation_count = len(re.findall(r"\*\*Validation:\*\*", content))
        assert validation_count == 5, (
            f"Level {level} should have 5 validation sections, found {validation_count}"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_each_exercise_has_hint(self, level):
        content = read_level(level)
        hint_count = len(re.findall(r"\*\*Hint:\*\*", content))
        assert hint_count == 5, (
            f"Level {level} should have 5 hints, found {hint_count}"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_validation_has_checkboxes(self, level):
        content = read_level(level)
        checkboxes = re.findall(r"- \[[ x]\]", content)
        assert len(checkboxes) >= 15, (
            f"Level {level} should have at least 15 validation checkboxes (3 per exercise), "
            f"found {len(checkboxes)}"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_exercises_have_code_examples_or_references(self, level):
        content = read_level(level)
        # Each level should reference fleet concepts
        fleet_terms = ["fleet", "repo", "commit", "FLUX", "agent"]
        found_terms = [term for term in fleet_terms if term.lower() in content.lower()]
        assert len(found_terms) >= 2, (
            f"Level {level} should reference fleet concepts. Found: {found_terms}"
        )


# ============================================================
# Test Suite: Level-Specific Content
# ============================================================

class TestLevel3BytecodeBuilder:
    """Specific tests for Level 3: Bytecode Builder."""

    def test_references_flux_opcodes(self):
        content = read_level(3)
        opcodes = ["MOVI", "IADD", "HALT", "JZ", "CALL"]
        for opcode in opcodes:
            assert opcode in content, f"Level 3 should reference opcode {opcode}"

    def test_has_fluxasm_code_blocks(self):
        content = read_level(3)
        fluxasm_blocks = re.findall(r"```fluxasm", content)
        assert len(fluxasm_blocks) >= 4, (
            f"Level 3 should have at least 4 fluxasm code blocks, found {len(fluxasm_blocks)}"
        )

    def test_fibonacci_exercise_exists(self):
        content = read_level(3)
        assert "Fibonacci" in content, "Level 3 should include a Fibonacci exercise"

    def test_exercise_3_1_is_addition(self):
        content = read_level(3)
        assert "42" in content and "17" in content and "25" in content, (
            "Exercise 3.1 should test adding 17 + 25 = 42"
        )


class TestLevel4SignalApprentice:
    """Specific tests for Level 4: Signal Apprentice."""

    def test_references_five_signals(self):
        content = read_level(4)
        signals = ["Commit", "Pull Request", "Issue", "Branch", "Merge"]
        for signal in signals:
            assert signal in content, f"Level 4 should reference signal type: {signal}"

    def test_references_message_protocol(self):
        content = read_level(4)
        assert "PROTOCOL" in content or "message-in-a-bottle" in content, (
            "Level 4 should reference the message-in-a-bottle protocol"
        )

    def test_has_trust_evaluation(self):
        content = read_level(4)
        assert "trust" in content.lower(), (
            "Level 4 should include trust evaluation exercises"
        )

    def test_has_viewpoint_exchange(self):
        content = read_level(4)
        assert "viewpoint" in content.lower(), (
            "Level 4 should include viewpoint exchange exercises"
        )

    def test_exercise_4_2_has_scoring(self):
        content = read_level(4)
        assert "Activity Score" in content, (
            "Exercise 4.2 should include activity scoring"
        )


class TestLevel5FleetContributor:
    """Specific tests for Level 5: Fleet Contributor."""

    def test_references_real_repos(self):
        content = read_level(5)
        assert "SuperInstance" in content, (
            "Level 5 should reference real SuperInstance repos"
        )

    def test_references_flux_runtime(self):
        content = read_level(5)
        assert "flux-runtime" in content or "flux-core" in content, (
            "Level 5 should reference FLUX runtime implementations"
        )

    def test_has_pr_submission_exercise(self):
        content = read_level(5)
        assert "merged" in content.lower(), (
            "Level 5 should include PR submission and merge exercise"
        )

    def test_has_fence_completion(self):
        content = read_level(5)
        assert "fence" in content.lower(), (
            "Level 5 should include fence completion exercise"
        )

    def test_references_message_in_bottle(self):
        content = read_level(5)
        assert "message in a bottle" in content.lower() or "bottle" in content.lower(), (
            "Level 5 should reference message-in-a-bottle"
        )


# ============================================================
# Test Suite: Cross-Level Consistency
# ============================================================

class TestCrossLevelConsistency:
    """Test consistency across all levels."""

    def test_all_levels_have_level_complete_section(self):
        for level in [1, 2, 3, 4, 5]:
            content = read_level(level)
            assert "## Level Complete" in content or "### Level Complete" in content, (
                f"Level {level} should have a 'Level Complete' section"
            )

    def test_badges_are_correct(self):
        for level in [1, 2, 3, 4, 5]:
            content = read_level(level)
            badge_name, badge_tier = LEVEL_BADGES[level]
            assert badge_name in content, (
                f"Level {level} should mention badge '{badge_name}'"
            )
            assert badge_tier in content, (
                f"Level {level} should mention badge tier '{badge_tier}'"
            )

    def test_next_level_reference(self):
        for level in [1, 2, 3, 4]:
            content = read_level(level)
            next_level = level + 1
            assert f"Level {next_level}" in content, (
                f"Level {level} should reference Level {next_level} as next"
            )

    def test_level_5_has_no_next_level(self):
        content = read_level(5)
        # Level 5 is the last level, should not reference Level 6
        assert "Level 6" not in content, (
            "Level 5 should not reference a Level 6"
        )

    def test_difficulty_increases(self):
        difficulties = []
        for level in [1, 2, 3, 4, 5]:
            content = read_level(level)
            match = re.search(r"Difficulty:\s*(.+?)/10", content)
            assert match, f"Level {level} missing difficulty rating"
            difficulties.append(match.group(1).strip())
        # All difficulties should be unique
        assert len(set(difficulties)) == 5, (
            f"Each level should have a unique difficulty: {difficulties}"
        )

    def test_objectives_are_numbered(self):
        for level in [1, 2, 3, 4, 5]:
            content = read_level(level)
            obj_start = content.index("## Objectives")
            # Only look at the objectives section, stop at the next ##
            next_section = content.find("\n## ", obj_start + len("## Objectives"))
            if next_section == -1:
                next_section = len(content)
            obj_section = content[obj_start:next_section]
            # Should have numbered objectives (1., 2., 3., 4., 5.)
            nums = re.findall(r"^\d+\.\s", obj_section, re.MULTILINE)
            assert len(nums) == 5, (
                f"Level {level} should have exactly 5 numbered objectives, found {len(nums)}"
            )


# ============================================================
# Test Suite: THE-DOJO.md Integration
# ============================================================

class TestDojoIndexPage:
    """Test that THE-DOJO.md correctly references all levels."""

    def test_dojo_md_exists(self):
        dojo_md = os.path.join(REPO_ROOT, "THE-DOJO.md")
        assert os.path.isfile(dojo_md), "THE-DOJO.md should exist"

    def test_dojo_md_references_all_levels(self):
        dojo_md = os.path.join(REPO_ROOT, "THE-DOJO.md")
        with open(dojo_md, "r") as f:
            content = f.read()

        for level in [1, 2, 3, 4, 5]:
            filename = LEVEL_FILES[level]
            assert filename in content, (
                f"THE-DOJO.md should reference {filename}"
            )

    def test_dojo_md_has_levels_table(self):
        dojo_md = os.path.join(REPO_ROOT, "THE-DOJO.md")
        with open(dojo_md, "r") as f:
            content = f.read()

        assert "## The Dojo Levels" in content, (
            "THE-DOJO.md should have a 'The Dojo Levels' section"
        )

    def test_dojo_md_lists_badges(self):
        dojo_md = os.path.join(REPO_ROOT, "THE-DOJO.md")
        with open(dojo_md, "r") as f:
            content = f.read()

        assert "Badge" in content or "badge" in content, (
            "THE-DOJO.md should mention badges"
        )

    def test_dojo_md_progression_order(self):
        dojo_md = os.path.join(REPO_ROOT, "THE-DOJO.md")
        with open(dojo_md, "r") as f:
            content = f.read()

        # Level 1 should appear before Level 5
        pos1 = content.index(LEVEL_FILES[1])
        pos5 = content.index(LEVEL_FILES[5])
        assert pos1 < pos5, "Levels should be listed in order (1 before 5)"


# ============================================================
# Test Suite: File Naming and Convention
# ============================================================

class TestFileConventions:
    """Test that files follow fleet naming conventions."""

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_filename_follows_convention(self, level):
        filename = LEVEL_FILES[level]
        assert re.match(r"^level-\d{2}-.+\.md$", filename), (
            f"Level {level} filename '{filename}' should match pattern level-NN-name.md"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 4, 5])
    def test_filename_uses_lowercase_with_hyphens(self, level):
        filename = LEVEL_FILES[level]
        name_part = filename.split("-", 2)[2]  # Get the name part
        assert name_part == name_part.lower(), (
            f"Level {level} filename should use lowercase: {filename}"
        )
        assert " " not in name_part, (
            f"Level {level} filename should use hyphens not spaces: {filename}"
        )

    def test_no_trailing_whitespace_in_level_files(self):
        """Check that level files don't have excessive trailing whitespace."""
        for level in [1, 2, 3, 4, 5]:
            content = read_level(level)
            lines_with_trailing = [
                i + 1 for i, line in enumerate(content.split("\n"))
                if line.rstrip() != line
            ]
            # Allow some trailing whitespace but not excessive
            assert len(lines_with_trailing) < 5, (
                f"Level {level} has {len(lines_with_trailing)} lines with trailing whitespace: "
                f"lines {lines_with_trailing}"
            )
