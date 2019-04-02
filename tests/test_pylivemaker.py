#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pylivemaker` package."""

from click.testing import CliRunner

from livemaker import cli


def test_lmar(shared_datadir):
    """Test lmar."""
    runner = CliRunner()

    # simple archive
    result = runner.invoke(cli.lmar, ['l', str(shared_datadir / 'test.dat')])
    assert result.exit_code == 0
    assert 'hello.txt' in result.output

    # simple exe
    result = runner.invoke(cli.lmar, ['l', str(shared_datadir / 'test.exe')])
    assert result.exit_code == 0
    assert 'hello.txt' in result.output

    # actual LiveMaker save file (from LiveNovel tutorial game)
    result = runner.invoke(cli.lmar, ['l', str(shared_datadir / 'save.dat')])
    assert result.exit_code == 0
    assert 'STATUSSAVEDATA' in result.output


def test_lmlsb(shared_datadir):
    """Test lmlsb."""
    runner = CliRunner()

    result = runner.invoke(cli.lmlsb, ['probe', str(shared_datadir / 'gamemain.lsb')])
    assert result.exit_code == 0
    assert 'LiveMaker compiled LSB script file' in result.output


def test_validate(shared_datadir):
    """Test lmlsb validation.

    This verifies that we can read/write both LSB and LiveNovel scripts that
    match LiveMaker's binaries.

    The sample LSB's used in these tests were generated by the most recent version of
    LiveMaker3 (setup03171228f.exe) and LiveNovel ADV-1 (adv-type1-03171228.exe).
    To generate your own test LSB's, just follow the tutorial from the LiveNovel docs.

    """
    runner = CliRunner()

    # LM3 ゲームメイン.lsb (from LiveNovel tutorial game)
    result = runner.invoke(cli.lmlsb, ['validate', str(shared_datadir / 'gamemain.lsb')])
    assert result.exit_code == 0

    # LM3 00000001.lsb (from LiveNovel tutorial game)
    result = runner.invoke(cli.lmlsb, ['validate', str(shared_datadir / '00000001.lsb')])
    assert result.exit_code == 0