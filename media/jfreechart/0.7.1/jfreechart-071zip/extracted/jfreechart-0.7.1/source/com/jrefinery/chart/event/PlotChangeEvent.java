/* =======================================
 * JFreeChart : a Java Chart Class Library
 * =======================================
 *
 * Project Info:  http://www.jrefinery.com/jfreechart;
 * Project Lead:  David Gilbert (david.gilbert@jrefinery.com);
 *
 * (C) Copyright 2000-2002, by Simba Management Limited and Contributors.
 *
 * This library is free software; you can redistribute it and/or modify it under the terms
 * of the GNU Lesser General Public License as published by the Free Software Foundation;
 * either version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this library;
 * if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
 * MA 02111-1307, USA.
 *
 * --------------------
 * PlotChangeEvent.java
 * --------------------
 * (C) Copyright 2000-2002, by Simba Management Limited.
 *
 * Original Author:  David Gilbert (for Simba Management Limited);
 * Contributor(s):   -;
 *
 * $Id: PlotChangeEvent.java,v 1.3 2001/11/12 09:02:31 mungady Exp $
 *
 * Changes (from 24-Aug-2001)
 * --------------------------
 * 24-Aug-2001 : Added standard source header. Fixed DOS encoding problem (DG);
 * 07-Nov-2001 : Updated e-mail address in header (DG);
 *
 */

package com.jrefinery.chart.event;

import com.jrefinery.chart.*;

/**
 * A change event that encapsulates information about a change to a plot.
 */
public class PlotChangeEvent extends ChartChangeEvent {

    /**
     * The plot that generated the event.
     */
    protected Plot plot;

    /**
     * Default constructor.
     * @param plot The plot that generated the event.
     */
    public PlotChangeEvent(Plot plot) {
        super(plot);
        this.plot = plot;
    }

}
