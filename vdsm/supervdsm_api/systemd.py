# Copyright 2016 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#
from __future__ import absolute_import

from vdsm import cmdutils
from vdsm import commands
from vdsm import utils

from . import expose


_SYSTEMCTL = utils.CommandPath("systemctl",
                               "/bin/systemctl",
                               "/usr/bin/systemctl",
                               )


_MACHINECTL = utils.CommandPath("machinectl",
                                "/bin/machinectl",
                                "/usr/bin/machinectl",
                                )


_ACCOUNTING = (
    cmdutils.Accounting.CPU,
    cmdutils.Accounting.Memory,
    cmdutils.Accounting.BlockIO,
)


@expose
def systemd_run(unit_name, cgroup_slice, *args):
    return commands.execCmd(
        cmdutils.systemd_run(
            args,
            unit=unit_name,
            slice=cgroup_slice,
            accounting=_ACCOUNTING,
        )
    )


@expose
def systemctl_stop(name):
    return commands.execCmd(
        [_SYSTEMCTL.cmd, 'stop', name],
    )


@expose
def machinectl_poweroff(name):
    return commands.execCmd(
        [_MACHINECTL.cmd, 'poweroff', name],
    )
