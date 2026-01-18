"""Tests for database module"""

import pytest
import os
import tempfile
from pathlib import Path
from sa.utils.database import Database
from sa.utils.projects import ProjectManager


@pytest.fixture
def temp_db():
    """Create temporary database for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "test.db")
        db = Database(db_path)
        yield db
        # Cleanup
        if os.path.exists(db_path):
            os.remove(db_path)


def test_create_project(temp_db):
    """Test project creation"""
    project_id = temp_db.create_project("Test Project", "Test Description")
    assert project_id > 0


def test_get_project(temp_db):
    """Test getting project"""
    project_id = temp_db.create_project("Test", "Desc")
    project = temp_db.get_project(project_id)
    assert project is not None
    assert project["name"] == "Test"
    assert project["description"] == "Desc"


def test_list_projects(temp_db):
    """Test listing projects"""
    temp_db.create_project("Project 1", "Desc 1")
    temp_db.create_project("Project 2", "Desc 2")
    projects = temp_db.get_projects()
    assert len(projects) == 2


def test_update_project(temp_db):
    """Test updating project"""
    project_id = temp_db.create_project("Old Name", "Old Desc")
    temp_db.update_project(project_id, "New Name", "New Desc")
    project = temp_db.get_project(project_id)
    assert project["name"] == "New Name"
    assert project["description"] == "New Desc"


def test_delete_project(temp_db):
    """Test deleting project"""
    project_id = temp_db.create_project("To Delete", "Desc")
    temp_db.delete_project(project_id)
    project = temp_db.get_project(project_id)
    assert project is None


def test_add_generation(temp_db):
    """Test adding generation"""
    project_id = temp_db.create_project("Test", "Desc")
    temp_db.add_generation(
        project_id, "image", "test prompt", "/path/to/image.png", 5.0
    )
    generations = temp_db.get_generations(project_id)
    assert len(generations) == 1
    assert generations[0]["type"] == "image"


def test_statistics(temp_db):
    """Test statistics tracking"""
    project_id = temp_db.create_project("Test", "Desc")

    # Add some generations
    temp_db.add_generation(project_id, "image", "prompt1", "/path/1.png", 2.0)
    temp_db.add_generation(project_id, "image", "prompt2", "/path/2.png", 3.0)
    temp_db.add_generation(project_id, "video", "prompt3", "/path/3.mp4", 10.0)

    # Get statistics
    stats = temp_db.get_statistics()
    assert stats["images_count"] == 2
    assert stats["videos_count"] == 1
    assert stats["total_time"] == 15.0
